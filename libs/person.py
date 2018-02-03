class Person():
    def __init__(self):
        self.emotion = Emotion()
        self.wellbeing = WellBeing()
        self.identity = Identity()

class Emotion():
    def __init__(self, valence=0, arousal=0):
        # Emotional Valence
        # This​ ​is​ ​an​ ​integer​ ​value​ ​from​ 1​ ​to​ 10​ ​that  expressed​ ​the​ ​strength​ ​of​ ​the​ ​sentiment​ ​(deviation​ ​from​ ​5,​ ​further  deviation​ ​=​ ​more​ ​strength)
        # ​​and​ ​positive​ ​or​ ​negative​ ​elements​ ​of​ ​the  emotion.​ 
        # ​Note :​ ​this​ ​may​ ​changing​ ​rapidly​ ​in​ ​the​ ​course​ ​of​ ​a​ ​few seconds
        self.valence = valence

        # Emotional Arousal
        # This​ ​is​ ​an​ ​integer​ ​value​ ​containing​ ​the​ ​value​ ​of​ ​how​ ​aroused​ ​that​ ​emotion is.
        # 1 = Low Arousal 10 = High Arousal
        self.arousal = arousal
    
class WellBeing():
    def __init__(self):
        # Mental Well Being
        self.mental = MentalWellBeing()
        # Physical Well Being
        self.physical = PhysicalWellBeing()

class PhysicalWellBeing(WellBeing):
    def __init__(self, sick = 1, tired = 1, hunger = 1, thirst=1):
        # Physical Sickness
        # An​ ​integer​ ​value​ ​of​ ​sickness​ ​felt​ ​at​ ​a​ ​given​ ​time.​
        # ​This​ ​is​ ​directly​ ​linked​ ​to  sentiment​ ​values​ ​overall​ ​and​ ​sentiment​ ​values​ ​of​ ​the​ ​entire​ ​experience, smell,​ ​and​ ​sight.​
        # ​These​ ​sentiment​ ​values​ ​are​ ​inversely​ ​related​ ​as​ ​the  sickness​ ​value​ ​rises​ ​the​ ​sentiment​ ​values​ ​drop.
        # 1 = Not Sick 10 = Terminal Illness
        self.sick = sick

        # Physical Tiredness
        # This​ ​is​ ​an​ ​integer​ ​value​ ​of​ ​the​ ​tiredness​ ​of​ ​the​ ​experience​ ​at​ ​a​ ​given​ ​time,  this​ ​has​ ​a​ ​large​ ​effect​ ​on​ ​the​ ​logic​ ​of​ ​Natural​ ​Language​ ​Processing​ ​of​ ​the  being.​ 
        # ​This​ ​raises​ ​the​ ​social​ ​anxiety​ ​variables​ ​and​ ​lowers​ ​the​ ​strength  variables.​ ​Arousal​ ​status​ ​is​ ​lowered​ ​significantly​ ​by​ ​this​ ​value​ ​raising.​ ​​
        # ​This  vaguely​ ​lowers​ ​overall​ ​sentiment​ ​values.
        # 1 = Awake 10 = Extreme Sleep Deprivation
        self.tired = tired

        # Physical Hunger
        # This​ ​is​ ​an​ ​integer​ ​value​ ​of​ ​the​ ​hunger​ ​value​ ​of​ ​the​ ​experience​ ​at​ ​a​ ​given  time.​ ​
        # This​ ​is​ ​generally​ ​used​ ​to​ ​redirect​ ​the​ ​purpose​ ​of​ ​the​ ​next​ ​experience and​ ​if​ ​this​ ​value​ ​gets​ ​to​ ​high​ ​sickness​ ​begins​ ​to​ ​rise​ ​as​ ​well.​
        # This​ ​value​ ​is  compressed​ ​immediately​ ​unless​ ​it​ ​deviates​ ​abnormally​ ​from​ ​1.
        # 1 = Normal 10 = Near Death Hunger
        self.hunger = hunger

        # Physical Thirst
        # This​ ​is​ ​an​ ​integer​ ​value​ ​of​ ​the​ thirst ​value​ ​of​ ​the​ ​experience​ ​at​ ​a​ ​given  time.​ ​
        # This​ ​is​ ​generally​ ​used​ ​to​ ​redirect​ ​the​ ​purpose​ ​of​ ​the​ ​next​ ​experience and​ ​if​ ​this​ ​value​ ​gets​ ​to​ ​high​ ​sickness​ ​begins​ ​to​ ​rise​ ​as​ ​well.​
        # This​ ​value​ ​is  compressed​ ​immediately​ ​unless​ ​it​ ​deviates​ ​abnormally​ ​from​ ​1.
        # 1 = Normal 10 = Near Death Thirst
        self.thirst = thirst

        self.addiction = PhysicalAddiction()


class PhysicalAddiction(PhysicalWellBeing):
    def __init__(self, level = 1, timesince = 0):
        self.level = level
        self.timesince = timesince

class MentalWellBeing(WellBeing):
    def __init__(self, sa = 5, strength = 5, satself = 5, satothers = 5, satpurp = 5, satspir = 5):
        # Social Anxiety
        # This​ ​is​ ​actually​ ​a​ ​very​ ​good​ ​measure​ ​of​ ​introvertedness​ ​vs​ ​extrovertedness,  this​ ​is​ ​an​ ​integer​ ​describing​ ​the​ ​anxiety​ ​of​ ​the​ ​person​ ​in​ ​social​ ​situations.   
        # 5​ ​=​ ​neutral​ ​1 ​=​ ​Extreme​ ​introvertedness​ ​10​ ​=​ ​Extreme  extrovertedness
        self.socialanxiety = sa
        
        # Strength of Emotions
        # The​ ​strength​ ​the​ ​emotions​ ​being​ ​felt,​ ​this​ ​affects​ ​all​ ​sentiment​ ​values  based​ ​on​ ​the​ ​emotion​ ​variables,​ ​and​ ​can​ ​alter​ ​sentiment​ ​values​ ​of​ ​certain  details​ ​of​ ​the​ ​experience
        # ​​5​ ​=​ ​neutral​ 10 ​=​ ​Emotions​ ​have​ ​taken​ ​over​ ​all  mental​ ​processes 1 = Pyschopathic behavior
        self.strength = strength

        # Satisfaction Variables
        # Satisfaction with Self largely effects emotional state
        # Satisfaction with Others effects social variables

        # Satisfaction with entity's self
        # This​ ​is​ ​an​ ​integer​ ​value​ ​containing​ ​the​ ​value​ ​of​ ​self​ ​satisfaction​ ​this​ ​is​ ​fed​ ​by  the​ ​other​ ​three​ ​securities​ 
        # ​and​ ​the​ ​average​ ​of​ ​the​ ​sentiment​ ​values​ ​of​ ​the  previous​ ​experiences​ ​that​ ​recently​ ​occurred 
        # 1 = Extreme insecurity 5 = Average 10 = Extreme Confidence
        self.satself = satself

        # Satisfaction with others
        # This​ ​is​ ​an​ ​integer​ ​value​ ​based​ ​on​ ​social​ ​anxiety​ ​and​ ​sentiment​ ​values​ ​from  the​ ​social​ ​general​ ​class,​ ​this​ ​feeds​ ​social​ ​anxiety​ ​variables
        # 1 = No trust in others 5 = Average Trust in Others 10 = Extreme trust in others
        self.satothers = satothers

        # Satisfaction with Purpose
        # This​ ​is​ ​an​ ​integer​ ​of​ ​the​ ​average​ ​sentiment​ ​values​ ​of​ ​the​ ​work​ ​experienced previously.
        # ​This​ ​is​ ​often​ ​compressed​ ​and​ ​placed​ ​in​ ​this​ ​variable​ ​as​ ​the  experiences​ ​of​ ​working​ ​break​ ​down.​ 
        # ​This​ ​affects​ ​general​ ​outlook​ ​on​ ​life​ ​and therefore​ ​is​ ​the​ ​basis​ ​of​ ​the​ ​sentiment​ ​variable​ ​found​ ​in​ ​emotion,​ ​and​ ​can affect​ ​reflection​ ​upon​ ​previous​ ​memories.
        # 1 = Has no purpose 10 = Is passionate about current occupation
        self.satpurp = satpurp

        # Satisfaction with Spiritual
        # This​ ​is​ ​an​ ​integer​ ​of​ ​the​ ​security​ ​within​ ​believed​ ​place​ ​in​ ​the​ ​universe,​ ​this can​ ​be​ ​any​ ​philosophy.​ 
        # ​If​ ​you​ ​are​ ​questioning​ ​your​ ​philosophical​ ​beliefs​ ​or are​ ​acting​ ​against​ ​believed​ ​philosophy​ ​this​ ​value​ ​goes​ ​down.​ 
        # ​This​ ​is​ ​tied​ ​to  purpose​ ​of​ ​experience​ ​and​ ​believed​ ​philosophy. 
        # 1 = Extreme questioning of spiritual and moral values 10 = Total Belief of Ideology
        self.satspir = satspir
    
class Identity():
    def __init__(self, name="John Doe"):
        # Name
        # Personal identifier of one's self
        self.name = name