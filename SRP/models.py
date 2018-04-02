from django.db import models

# Create your models here.
class Entity(models.Model):
    class Meta:
    permissions = (
      ("man_entity", "Can manipulate Entity"),
    )
    # Identification Attributes
    name = models.TextField()
    current_t = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Emotional Attributes
    # Fun and Happiness are the same
    joy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sadness = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    fear = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    anger = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    analytical = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    confident = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    tentative = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    '''
joy
sadness
fear 
anger
analytical
confident
tentative
    '''

class Experience(models.Model):
    class Meta:
    permissions = (
      ("man_experience", "Can manipulate Experience"),
    )
    # Identification Attributes
    name = models.TextField()
    content = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    create_t = models.IntegerField(default=0)
    process_t = models.IntegerField(default=-1)

    # Emotional Attributes
    # Fun and Happiness are the same
    joy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sadness = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    fear = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    anger = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    analytical = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    confident = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    tentative = models.DecimalField(default=0, max_digits=20, decimal_places=15)

class Sentence(models.Model):
    class Meta:
    permissions = (
      ("man_sent", "Can manipulate Sentence"),
    )
    content = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField(default=0)
    process_t = models.IntegerField(default=-1)

    # Emotional Attributes
    # Fun and Happiness are the same
    joy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sadness = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    fear = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    anger = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    analytical = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    confident = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    tentative = models.DecimalField(default=0, max_digits=20, decimal_places=15)

class Noun(models.Model):
    class Meta:
    permissions = (
      ("man_noun", "Can manipulate Noun"),
    )
    noun = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField(default=0)
    process_t = models.IntegerField(default=-1)

    # Emotional Attributes
    # Fun and Happiness are the same
    joy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sadness = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    fear = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    anger = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    analytical = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    confident = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    tentative = models.DecimalField(default=0, max_digits=20, decimal_places=15)