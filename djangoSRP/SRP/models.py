from django.db import models

# Create your models here.
class Entity(models.Model):
    # Identification Attributes
    name = models.TextField()
    current_t = models.IntegerField(default=0)

    # Overall Sentiment Scores
    sent_score = models.IntegerField(default=0)
    sent_mag = models.IntegerField(default=0)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.IntegerField(default=0)
    emo_sad = models.IntegerField(default=0)
    emo_suprised = models.IntegerField(default=0)
    # Hatred and Anger are the same
    emo_angry = models.IntegerField(default=0)
    emo_bored = models.IntegerField(default=0)
    emo_empty = models.IntegerField(default=0)
    emo_enthusiasm = models.IntegerField(default=0)
    emo_neutral = models.IntegerField(default=0)
    emo_worry = models.IntegerField(default=0)
    emo_love = models.IntegerField(default=0)

    '''
     emo_happy
    emo_sad
    emo_suprised 
    emo_angry
    emo_bored
    emo_empty
    emo_enthusiasm
    emo_neutral
    emo_worry
    emo_love
    '''

class Experience(models.Model):
    # Identification Attributes
    name = models.TextField()
    content = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    create_t = models.IntegerField()

    # Overall Sentiment Scores
    sent_score = models.IntegerField(default=0)
    sent_mag = models.IntegerField(default=0)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.IntegerField(default=0)
    emo_sad = models.IntegerField(default=0)
    emo_suprised = models.IntegerField(default=0)
    # Hatred and Anger are the same
    emo_angry = models.IntegerField(default=0)
    emo_bored = models.IntegerField(default=0)
    emo_empty = models.IntegerField(default=0)
    emo_enthusiasm = models.IntegerField(default=0)
    emo_neutral = models.IntegerField(default=0)
    emo_worry = models.IntegerField(default=0)
    emo_love = models.IntegerField(default=0)

class Sentence(models.Model):
    content = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField()

    # Overall Sentiment Scores
    sent_score = models.IntegerField(default=0)
    sent_mag = models.IntegerField(default=0)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.IntegerField(default=0)
    emo_sad = models.IntegerField(default=0)
    emo_suprised = models.IntegerField(default=0)
    # Hatred and Anger are the same
    emo_angry = models.IntegerField(default=0)
    emo_bored = models.IntegerField(default=0)
    emo_empty = models.IntegerField(default=0)
    emo_enthusiasm = models.IntegerField(default=0)
    emo_neutral = models.IntegerField(default=0)
    emo_worry = models.IntegerField(default=0)
    emo_love = models.IntegerField(default=0)

class Noun(models.Model):
    noun = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField()

    # Overall Sentiment Scores
    sent_score = models.IntegerField(default=0)
    sent_mag = models.IntegerField(default=0)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.IntegerField(default=0)
    emo_sad = models.IntegerField(default=0)
    emo_suprised = models.IntegerField(default=0)
    # Hatred and Anger are the same
    emo_angry = models.IntegerField(default=0)
    emo_bored = models.IntegerField(default=0)
    emo_empty = models.IntegerField(default=0)
    emo_enthusiasm = models.IntegerField(default=0)
    emo_neutral = models.IntegerField(default=0)
    emo_worry = models.IntegerField(default=0)
    emo_love = models.IntegerField(default=0)