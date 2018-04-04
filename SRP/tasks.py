# Create your tasks here
from __future__ import absolute_import, unicode_literals
from .models import Entity, Experience, Sentence, Noun
from decimal import Decimal
from .libs.nlp import tone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from background_task import background
from textblob import TextBlob

# Sample Tasks
def add(x, y):
    return x + y


def div(x, y):
    return x / y


def xsum(numbers):
    return sum(numbers)

@background(schedule=1)
def experience_preprocessing(text, title, entity_id, current_t):
    t = TextBlob(text)

    addition = 0
    explist = []
    while True:
        exp = t.sentences[0+addition: 99+addition]
        if exp:
            explist.append(exp)
            addition =+ 100
        else:
            break

    count = 1
    for j in explist:
        a = str()
        for i in j:
            stri = str(i)
            a = a + " " + stri
        name = title + " " + str(count)
        e = Experience(name=name, content=a, entity_id=entity_id, create_t=entity_current_t)
        e.save()
        experience_intake(e.id, entity.current_t)
    
    return True

@background(schedule=1)
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

def noun_display(noun, entity_id):
    context = dict()
    nounlist = Noun.objects.filter(entity_id=entity_id, noun=noun)

    if nounlist.count() == 0:
        context.update(search_error=(noun + " was not found."))
        return context

    # Average Scores
    '''
    avg_score
    avg_mag
    avg_emo_happy
    avg_emo_sad
    avg_emo_suprised 
    avg_emo_angry
    avg_emo_bored
    avg_emo_empty
    avg_emo_enthusiasm
    avg_emo_neutral
    avg_emo_worry
    avg_emo_love
    '''
    avg_score = Decimal()
    avg_mag = Decimal()
    avg_emo_happy = Decimal()
    avg_emo_sad = Decimal()
    avg_emo_suprised  = Decimal()
    avg_emo_angry = Decimal()
    avg_emo_bored = Decimal()
    avg_emo_empty = Decimal()
    avg_emo_enthusiasm = Decimal()
    avg_emo_neutral = Decimal()
    avg_emo_worry = Decimal()
    avg_emo_love = Decimal()
    for rec in nounlist:
        avg_score += rec.sent_score
        avg_mag += rec.sent_mag   
        avg_emo_happy += rec.emo_happy
        avg_emo_sad += rec.emo_sad       
        avg_emo_suprised += rec.emo_suprised
        avg_emo_angry += rec.emo_angry
        avg_emo_bored += rec.emo_bored
        avg_emo_empty += rec.emo_empty
        avg_emo_enthusiasm += rec.emo_enthusiasm
        avg_emo_neutral += rec.emo_neutral
        avg_emo_worry += rec.emo_worry
        avg_emo_love += rec.emo_love

    avg_score /= nounlist.count()
    avg_mag /= nounlist.count()
    avg_emo_happy /= nounlist.count()
    avg_emo_sad /= nounlist.count()
    avg_emo_suprised /= nounlist.count()
    avg_emo_angry /= nounlist.count()
    avg_emo_bored /= nounlist.count()
    avg_emo_empty /= nounlist.count()
    avg_emo_enthusiasm /= nounlist.count()
    avg_emo_neutral /= nounlist.count()
    avg_emo_worry /= nounlist.count()
    avg_emo_love /= nounlist.count()

    context.update(noun_name=noun, noun_score=avg_score, noun_mag=avg_mag, noun_emo_happy=avg_emo_happy, noun_emo_sad=avg_emo_sad, noun_emo_suprised=avg_emo_suprised, noun_emo_angry=avg_emo_angry, noun_emo_bored=avg_emo_bored, noun_emo_empty=avg_emo_empty, noun_emo_enthusiasm=avg_emo_enthusiasm, noun_emo_neutral=avg_emo_neutral, noun_emo_worry=avg_emo_worry, noun_emo_love=avg_emo_love)
    return context