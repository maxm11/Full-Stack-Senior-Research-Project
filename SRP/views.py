from django.shortcuts import render, get_object_or_404  
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entity, Experience, Sentence, Noun
from .tasks import experience_intake, noun_display, entity_bg
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def gen_nbar_context():
    entitylist = Entity.objects.order_by('-name')
    context = {'entitylist' : entitylist}
    return context

@login_required
def createEntity(request):
    context = gen_nbar_context()
    context.update(nbar='home')
    return render(request, 'SRP/createEntity.html', context)

@login_required
@permission_required('SRP.man_entity')
def create(request):
    try:
        name = request.POST['name']
        joy = request.POST['joy']
        sadness = request.POST['sadness']
        fear  = request.POST['fear']
        anger = request.POST['anger']
        analytical = request.POST['analytical']
        confident = request.POST['confident']
        tentative = request.POST['tentative']
    except KeyError:
        context = gen_nbar_context()
        context.update(error_message='Please fill all fields.')
        return render(request, 'SRP/createEntity.html', context)
    else:
        e = Entity(name=name,joy=joy,sadness=sadness,fear=fear,anger=anger,analytical=analytical,confident=confident,tentative=tentative)
        e.save()
        entity_bg(e.id)
        return HttpResponseRedirect(reverse('dashEntity', args=(e.id,)))

@login_required
def addExperience(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    context = gen_nbar_context()
    context.update(entity=entity)
    return render(request, 'SRP/createExperience.html', context)

@login_required
@permission_required('man_experience')
def add(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    try:
        name = request.POST['prod_name']
        content = request.POST['prod_content']
        time = entity.current_t
    except KeyError:
        context = gen_nbar_context()
        context.update(entity=entity)
        return render(request, 'SRP/createExperience.html', context)
    else:
        e = Experience(name=name, content=content, entity_id=entity.id, create_t=time)
        e.save()
        experience_intake(e.id, entity.current_t)
        return HttpResponseRedirect(reverse('dashExperience', args=(entity.id, e.id)))

@login_required
@permission_required("man_entity")
def purge(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    entity.delete()

    return HttpResponseRedirect(reverse('createEntity'), args=(entity.id, ))

@login_required
@permission_required("man_experience")
def deleteExperience(request, entity_id, exp_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experience = get_object_or_404(Experience, pk=exp_id, entity_id=entity_id)
    experience.delete()

    return HttpResponseRedirect(reverse('createEntity'), args=(entity.id, ))

@login_required
def dashEntity(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experiencelist = Experience.objects.filter(entity_id=entity.id).order_by('pk')[:5]
    # Time Step Variables
    sentcount = Sentence.objects.filter(entity_id=entity.id).count()
    try:
        t_width = entity.current_t/sentcount
    except ZeroDivisionError:
        t_width = 0
    context = gen_nbar_context()
    context.update(entity=entity, experiencelist=experiencelist, sentcount=sentcount, t_width=t_width)
    return render(request, 'SRP/entityDashPre.html', context)

@login_required
@permission_required('man_entity')
def toggle(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    entity.current_process = not entity.current_process

    return HttpResponseRedirect('dashEntity', args=(entity.id, ))

@login_required
@permission_required('man_noun')
def noun_search(request, entity_id):
    # Implementation Alert
    # Implement Time
    search = request.POST['search']
    entity = get_object_or_404(Entity, pk=entity_id)
    experiencelist = Experience.objects.filter(entity_id=entity.id).order_by('pk')[:5]
    sentcount = Sentence.objects.filter(entity_id=entity.id).count()
    context = gen_nbar_context()
    context.update(entity=entity, experiencelist=experiencelist, sentcount=sentcount)
    dic = noun_display(search, entity.id)
    res = dic
    context.update(res)
    try:
        context['search_error']
        return render(request, 'SRP/entityDashPre.html', context)
    except KeyError:
        return render(request, 'SRP/entityDashPost.html', context)

@login_required
def dashExperience(request, experience_id, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experience = get_object_or_404(Experience, pk=experience_id, entity_id=entity_id)
    sentlist = Sentence.objects.filter(entity_id=entity.id, experience_id=experience.id).order_by('pk')[:5]
    context = gen_nbar_context()
    context.update(entity=entity, experience=experience, sentlist=sentlist)
    return render(request, 'SRP/experienceDash.html', context)

@login_required
def experienceList(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experiencelist = Experience.objects.filter(entity_id=entity.id).order_by('pk')
    context = gen_nbar_context()
    context.update(entity=entity, experiencelist=experiencelist)
    return render(request, 'SRP/experienceList.html', context)

@login_required
def sentenceList(request, entity_id, experience_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    experience = get_object_or_404(Experience, pk=experience_id, entity_id=entity_id)
    sentlist = Sentence.objects.filter(entity_id=entity.id, experience_id=experience.id).order_by('pk')
    context = gen_nbar_context()
    context.update(entity=entity, experience=experience, sentlist=sentlist)
    return render(request, 'SRP/sentenceList.html', context)

@login_required
def editEntity(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    context = gen_nbar_context()
    context.update(entity=entity)
    return render(request, 'SRP/editEntity.html', context)