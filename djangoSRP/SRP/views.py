from django.shortcuts import render, get_object_or_404  
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entity, Experience, Sentence

# Create your views here.
def gen_nbar_context():
    entitylist = Entity.objects.order_by('-name')
    context = {'entitylist' : entitylist}
    return context

def createEntity(request):
    context = gen_nbar_context()
    context.update(nbar='home')
    return render(request, 'SRP/createEntity.html', context)

def create(request):
    try:
        name = request.POST['name']
        emo_happy = request.POST['happy']
        emo_sad = request.POST['sad']
        emo_suprised = request.POST['suprise']
        emo_angry = request.POST['angry']
        emo_bored = request.POST['bored']
        emo_empty = request.POST['empty']
        emo_enthusiasm = request.POST['enthusiasm']
        emo_neutral = request.POST['neutral']
        emo_worry = request.POST['worry']
        emo_love = request.POST['love']
    except KeyError:
        context = gen_nbar_context()
        context.update(error_message='Please fill all fields.')
        return render(request, 'SRP/createEntity.html', context)
    else:
        e = Entity(name=name, emo_angry=emo_angry, emo_bored=emo_bored, emo_empty=emo_empty, emo_enthusiasm=emo_enthusiasm, emo_happy=emo_happy, emo_love=emo_love, emo_neutral=emo_neutral, emo_sad=emo_sad, emo_suprised=emo_suprised, emo_worry=emo_worry)
        e.save()
        return HttpResponseRedirect(reverse('dashEntity', args=(e.id,)))

def addExperience(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    context = gen_nbar_context()
    context.update(entity=entity)
    return render(request, 'SRP/createExperience.html', context)

def add(request, entity_id):
    try:
        name = request.POST['prod_name']
        content = request.POST['prod_content']
    
    except KeyError:
        entity = get_object_or_404(Entity, pk=entity_id)
        context = gen_nbar_context()
        context.update(entity=entity)
        return render(request, 'SRP/createExperience.html', context)
    else:
        entity = get_object_or_404(Entity, pk=entity_id)
        e = Experience(name=name, content=content, entity_id=entity.id)
        e.save()
        return HttpResponseRedirect(reverse('dashExperience', args=(e.id, entity.id)))

def dashEntity(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experiencelist = Experience.objects.filter(entity_id=entity.id).order_by('pk')[:5]
    sentcount = Sentence.objects.filter(entity_id=entity.id).count()
    context = gen_nbar_context()
    context.update(entity=entity, experiencelist=experiencelist, sentcount=sentcount)
    return render(request, 'SRP/entityDash.html', context)

def dashExperience(request, experience_id, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experience = get_object_or_404(Experience, pk=experience_id, entity_id=entity_id)
    context = gen_nbar_context()
    context.update(entity=entity)
    context.update(experience=experience)
    return render(request, 'SRP/experienceDash.html', context)

def editEntity(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    context = gen_nbar_context()
    context.update(entity=entity)
    return render(request, 'SRP/editEntity.html', context)

def index(request):
    return True