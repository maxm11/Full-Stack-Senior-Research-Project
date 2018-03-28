from django.db import models

# Create your models here.
class Entity(models.Model):
    # Identification Attributes
    name = models.TextField()
    current_t = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Overall Sentiment Scores
    sent_score = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sent_mag = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_sad = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_suprised = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    emo_angry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_bored = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_empty = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_enthusiasm = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_neutral = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_worry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_love = models.DecimalField(default=0, max_digits=20, decimal_places=15)

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
    create_t = models.IntegerField(default=0) 

    # Overall Sentiment Scores
    sent_score = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sent_mag = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_sad = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_suprised = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    emo_angry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_bored = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_empty = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_enthusiasm = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_neutral = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_worry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_love = models.DecimalField(default=0, max_digits=20, decimal_places=15)

class Sentence(models.Model):
    content = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField(default=0)

    # Overall Sentiment Scores
    sent_score = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sent_mag = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_sad = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_suprised = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    emo_angry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_bored = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_empty = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_enthusiasm = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_neutral = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_worry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_love = models.DecimalField(default=0, max_digits=20, decimal_places=15)

class Noun(models.Model):
    noun = models.TextField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    create_t = models.IntegerField(default=0)

    # Overall Sentiment Scores
    sent_score = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    sent_mag = models.DecimalField(default=0, max_digits=20, decimal_places=15)

    # Emotional Attributes
    # Fun and Happiness are the same
    emo_happy = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_sad = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_suprised = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    # Hatred and Anger are the same
    emo_angry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_bored = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_empty = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_enthusiasm = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_neutral = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_worry = models.DecimalField(default=0, max_digits=20, decimal_places=15)
    emo_love = models.DecimalField(default=0, max_digits=20, decimal_places=15)