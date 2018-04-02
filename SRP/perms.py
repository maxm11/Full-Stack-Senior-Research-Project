from .models import Entity, Experience, Noun
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Entity)
permission = Permission.objects.create(
    codename='man_entity',
    name='Can Manipulate Entity',
    content_type=content_type,
)

content_type = ContentType.objects.get_for_model(Experience)
permission = Permission.objects.create(
    codename='man_experience',
    name='Can Manipulate Experience',
    content_type=content_type,
)

content_type = ContentType.objects.get_for_model(Noun)
permission = Permission.objects.create(
    codename='man_noun',
    name='Can Manipulate Noun',
    content_type=content_type,
)