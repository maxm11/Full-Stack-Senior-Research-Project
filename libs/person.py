class Person():
    def __init__(self):
        self.emotion = Emotion()

class Emotion():
    """
    Class : Emotions
    """
    def __init__(self, valence=0, arousal=0):
        self.valence = valence
        self.arousal = arousal

        self.wellbeing = WellBeing()
    
class WellBeing():
    def __init__(self):
        # Scale from 1 - 10
        # Deviation from average(5) exhibits traits about person
        # Mental Variables
        self.mental = MentalWellBeing()
        self.physical = PhysicalWellBeing()

class PhysicalWellBeing(WellBeing):
    def __init__(self, sick = 1, tired = 1, hunger = 1, thirst=1, strength = 1, isAddict = 0):
        self.sick = sick
        self.tired = tired
        self.hunger = hunger
        self.strength = strength
        self.isAddict = isAddict


class MentalWellBeing(WellBeing):
    def __init__(self, sa =5, strength = 5, satself = 5, satothers = 5, satpurp = 5, satspir = 5):
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
    
