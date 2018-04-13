# Create your tasks here
from __future__ import absolute_import, unicode_literals
from .models import Entity, Experience, Sentence, Noun
from decimal import Decimal
from .libs.nlp import tone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from background_task import background
from textblob import TextBlob
from django_dandelion.datatxt import EntityExtraction
import requests

# Sample Tasks
def add(x, y):
    return x + y


def div(x, y):
    return x / y


def xsum(numbers):
    return sum(numbers)

@background(schedule=1, queue="entity")
def entity_bg(ent_id):
    entity_id = int(ent_id)
    entity = Entity.objects.filter(pk=entity_id)[0]

    if entity.current_process:
        try:
            sent = Sentence.objects.filter(entity_id=entity.id, process_t=-1)[0]
            ee = EntityExtraction()
            text = sent.content
            ee.params = 'text', text
            ee.params = 'lang', 'en'
            ee.params = 'country', 'US'
            ee.params = 'min_confidence', '0.5'
            a = ee.analyze()
            for note in a.annotations:
                n = Noun()
                n.noun = note['id']
                n.joy = sent.joy
                n.sadness = sent.sadness
                n.fear = sent.fear
                n.anger = sent.anger
                n.analytical = sent.analytical
                n.confident = sent.confident
                n.tentative = sent.tentative
                n.entity_id = entity.id
                n.experience_id = sent.experience_id
                n.sentence_id = sent.id
                n.save()
            sent.process_t = entity.current_t
            sent.save()
            entity.current_t += 1
            entity.joy = ((sent.joy + entity.joy)/2)
            entity.sadness = ((sent.sadness + entity.sadness)/2)
            entity.fear = ((sent.fear + entity.fear)/2)
            entity.anger = ((sent.anger + entity.anger)/2)
            entity.analytical = ((sent.analytical + entity.analytical)/2)
            entity.confident = ((sent.confident + entity.confident)/2)
            entity.tentative = ((sent.tentative + entity.tentative)/2)
            entity.save()
        except IndexError:
            entity.current_process = False
            entity.save()


@background(schedule=1, queue="experience")
def experience_intake(exp_id, time):
    experience_id = int(exp_id)
    experience = Experience.objects.filter(pk=experience_id)[0]

    # Take in Experience
    experience_content = experience.content

    # Run Text Sentiment
    # Output : sent_score, sent_mag, sentences[list]
    analysis = tone(experience_content)

    # Document Sentiment
    for t in analysis['document_tone']['tones']:
        tid = t['tone_id']
        score = t['score']
        exec("experience." + tid + "=  score")


    # Save Experience
    experience.process_t = time
    experience.save()

    # Breakdown the sentences and save them to the database
    if analysis['sentences_tone']:
        for sent in analysis['sentences_tone']:
            content = sent['text']
            s = Sentence(content=content, experience_id=experience.id, entity_id=experience.entity_id, create_t=time)
            for t in sent['tones']:
                tid = t['tone_id']
                score = t['score']
                exec("s." + tid + "=  score")
            s.save()

def noun_display(search, entity_id):
    # Establish Context
    context = dict()

    ee = EntityExtraction()
    text = search
    ee.params = 'text', text
    ee.params = 'lang', 'en'
    ee.params = 'country', 'US'
    ee.params = 'min_confidence', '0.01'
    a = ee.analyze()

    if a.annotations:
        concept = a.annotations[0]
        concept_title = concept['title']
        concept_id = concept['id']
        concept_confidence = concept['confidence']
        try:
            params = {'action':'query', 'titles': concept_title, 'prop':'pageimages', 'format':'json', 'pithumbsize':'256'}
            wiki_request = requests.post('https://en.wikipedia.org/w/api.php', params)
            j = wiki_request.json()
            concept_img = next( iter( (j['query']['pages'].values())))['thumbnail']['source']
        except:
            concept_img = ""
        
        try:
            params = {'action':'query', 'titles': concept_title, 'prop':'extracts', 'format':'json', 'exsentences':'2', 'explaintext':''}
            r = requests.post('https://en.wikipedia.org/w/api.php', params)
            j = r.json()
            concept_desc = next( iter( (j['query']['pages'].values())))['extract']

        except:
            concept_desc = ""
    else:
        context.update(search_error=(search + " is not a recognized concept."))
        return context


    # Get list of nouns
    nounlist = Noun.objects.filter(entity_id=entity_id, noun=concept_id)

    if nounlist:
        # Average Scores
        avg_joy = Decimal()
        avg_sadness = Decimal()
        avg_fear  = Decimal()
        avg_anger = Decimal()
        avg_analytical = Decimal()
        avg_confident = Decimal()
        avg_tentative = Decimal()
        for rec in nounlist:
            avg_joy += rec.joy
            avg_sadness += rec.sadness
            avg_fear  += rec.fear
            avg_anger += rec.anger
            avg_analytical += rec.analytical
            avg_confident += rec.confident
            avg_tentative += rec.tentative

        avg_joy /= nounlist.count()
        avg_sadness /= nounlist.count()
        avg_fear  /= nounlist.count()
        avg_anger /= nounlist.count()
        avg_analytical /= nounlist.count()
        avg_confident /= nounlist.count()
        avg_tentative /= nounlist.count()

        context.update(avg_joy = avg_joy, avg_sadness = avg_sadness, avg_fear  = avg_fear, avg_anger = avg_anger, avg_analytical = avg_analytical, avg_confident = avg_confident, avg_tentative = avg_tentative, concept_title=concept_title, concept_confidence=concept_confidence, concept_img=concept_img, concept_desc=concept_desc)
        return context

    else:
        context.update(search_error=(concept_title + " is a recognized concept but was not present in the selected entity."))
        return context

    