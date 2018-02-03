from libs.person import Person
import tkinter as tk
from tkinter import ttk, END, StringVar, Toplevel, filedialog, messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Application():
    def __init__(self, master=None):
        content = ttk.Frame(master)
        content.grid(column=0, row=0)
        self.mainProgram(content)
        self.master = master

    def mainProgram(self, master):
        # Title Label
        ltitle1 = ttk.Label(master, text="Computational​ ​Interpretation​ ​of​ ​Experience​ ​:​ ​The​ ​Foundations​ ​of​ ​Artificial​ ​Intelligence")
        # By Line
        lbyline1 = ttk.Label(master, text="By Max Murphy")

        # Create a Person Button
        bcreate1 = ttk.Button(master, text="Create a Person", command=self.createentity)

        # Load a Person Button
        bload1 = ttk.Button(master, text="Load a Person")
        
        # Save a Person Button
        bsave1 = ttk.Button(master, text="Save Person")

        # Configure Person Button
        bconfig1 = ttk.Button(master, text="Configure Person", command=self.configureentity)
        
        # Grid
        # Row 0
        ltitle1.grid(column=0, row=0, columnspan=4)
        # Row 1
        lbyline1.grid(column=0, row=1, columnspan=4)
        # Row 2
        bcreate1.grid(column=0, row=2)
        bload1.grid(column=1, row=2)
        bsave1.grid(column=2, row=2)
        bconfig1.grid(column=3, row=2)

    def configureentity(self, master=None):
        try:
            vars(self.person)
        except AttributeError:
            messagebox.showinfo(message='No Person is Loaded. Unable to configure')
            return None
        if master is None:
            master = self.master
        self.configwindow = Toplevel(master)
        self.configwindow.title("Configure Entity")
        configcontent = ttk.Frame(self.configwindow)
        configcontent.grid(column=0, row=0)
        
        # Title Label
        ltitle2 = ttk.Label(configcontent, text="Configure Entity")

        # Identity
        # Section Header Label
        lidentity1 = ttk.Label(configcontent, text="Identity Variables")

        # Name Entry Row
        lconfigi1 = ttk.Label(configcontent, text="Name")
        self.econfigi1 = ttk.Entry(configcontent)
        self.econfigi1.insert(END, self.person.identity.name)

        # Emotion
        # Section Header Label
        lemotion1 = ttk.Label(configcontent, text="Emotion Variables")

        # Valence Entry Row
        lconfige1 = ttk.Label(configcontent, text="Valence")
        self.econfige1 = ttk.Entry(configcontent)
        self.econfige1.insert(END, self.person.emotion.valence)

        # Arousal Entry Row
        lconfige2 = ttk.Label(configcontent, text="Arousal")
        self.econfige2 = ttk.Entry(configcontent)
        self.econfige2.insert(END, self.person.emotion.arousal)

        # Well Being
        # Section Header Label
        lwell1 = ttk.Label(configcontent, text="Well-Being Variables")

        # Physical Well-Being
        lphys1 = ttk.Label(configcontent, text="Physical Well-Being Variables")

        # Sickness Entry Row
        lconfigphys1 = ttk.Label(configcontent, text="Sickness Level")
        self.econfigwp1 = ttk.Entry(configcontent)
        self.econfigwp1.insert(END, self.person.wellbeing.physical.sick)

        # Tired Entry Row
        lconfigphys2 = ttk.Label(configcontent, text="Tiredness Level")
        self.econfigwp2 = ttk.Entry(configcontent)
        self.econfigwp2.insert(END, self.person.wellbeing.physical.tired)

        # Hunger Entry Row
        lconfigphys3 = ttk.Label(configcontent, text="Hunger Level")
        self.econfigwp3 = ttk.Entry(configcontent)
        self.econfigwp3.insert(END, self.person.wellbeing.physical.hunger)

        # Thirst Entry Row
        lconfigphys4 = ttk.Label(configcontent, text="Thirst Level")
        self.econfigwp4 = ttk.Entry(configcontent)
        self.econfigwp4.insert(END, self.person.wellbeing.physical.thirst)

        # Physical Addiction
        laddict1 = ttk.Label(configcontent, text="Physical Addiction Variables")

        # Addicition Level Entry Row
        lconfigwpa1 = ttk.Label(configcontent, text="Level of Addiction : ")
        self.econfigwpa1 = ttk.Entry(configcontent)
        self.econfigwpa1.insert(END, self.person.wellbeing.physical.addiction.level)

        # Time Since Last Dose Entry Row
        lconfigwpa2 = ttk.Label(configcontent, text="Time Since Last Dose : ")
        self.econfigwpa2 = ttk.Entry(configcontent)
        self.econfigwpa2.insert(END, self.person.wellbeing.physical.addiction.timesince)

        # Mental Well-Being
        lmental1 = ttk.Label(configcontent, text="Mental Well-Being Variables")

        # Social Anxiety Entry Row
        lconfigmental1 = ttk.Label(configcontent, text="Social Anxiety")
        self.econfigmental1 = ttk.Entry(configcontent)
        self.econfigmental1.insert(END, self.person.wellbeing.mental.socialanxiety)

        # Strength of Emotions Entry Row
        lconfigmental2 = ttk.Label(configcontent, text="Strength of Emotions")
        self.econfigmental2 = ttk.Entry(configcontent)
        self.econfigmental2.insert(END, self.person.wellbeing.mental.strength)

        # Satisfaction Variables
        # Satisfaction with Self
        lconfigmental3 = ttk.Label(configcontent, text="Satisfaction with Self")
        self.econfigmental3 = ttk.Entry(configcontent)
        self.econfigmental3.insert(END, self.person.wellbeing.mental.satself)

        # Satisfaction with Others
        lconfigmental4 = ttk.Label(configcontent, text="Satisfaction with Others")
        self.econfigmental4 = ttk.Entry(configcontent)
        self.econfigmental4.insert(END, self.person.wellbeing.mental.satothers)

        # Satisfaction with Purpose
        lconfigmental5 = ttk.Label(configcontent, text="Satisfaction with Purpose")
        self.econfigmental5 = ttk.Entry(configcontent)
        self.econfigmental5.insert(END, self.person.wellbeing.mental.satpurp)

        # Satisfaction with Beliefs
        lconfigmental6 = ttk.Label(configcontent, text="Satisfaction with Beliefs")
        self.econfigmental6 = ttk.Entry(configcontent)
        self.econfigmental6.insert(END, self.person.wellbeing.mental.satspir)

        # Apply Button
        bapply1 = ttk.Button(configcontent, text="Apply", command=self.applychanges)

        # Gridding
        # Row 0
        ltitle2.grid(column=0, row=0, columnspan=2)
        # Row 1
        lidentity1.grid(column=0, row=1, columnspan=2)
        # Row 2
        lconfigi1.grid(column=0, row=2)
        self.econfigi1.grid(column=1, row=2)
        # Row 3
        lemotion1.grid(column=0, row=3, columnspan=2)
        # Row 4
        lconfige1.grid(column=0, row=4)
        self.econfige1.grid(column=1, row=4)
        # Row 5
        lconfige2.grid(column=0, row=5)
        self.econfige2.grid(column=1, row=5)
        # Row 6
        lwell1.grid(column=0, row=6, columnspan=2)
        # Row 7
        lphys1.grid(column=0, row=7, columnspan=2)
        # Row 8
        lconfigphys1.grid(column=0, row=8)
        self.econfigwp1.grid(column=1, row=8)
        # Row 9
        lconfigphys2.grid(column=0, row=9)
        self.econfigwp2.grid(column=1, row=9)
        # Row 10
        lconfigphys3.grid(column=0, row=10)
        self.econfigwp3.grid(column=1, row=10)
        # Row 11
        lconfigphys4.grid(column=0, row=11)
        self.econfigwp4.grid(column=1, row=11)
        # Row 12
        laddict1.grid(column=0, row=12, columnspan=2)
        # Row 13
        lconfigwpa1.grid(column=0, row=13)
        self.econfigwpa1.grid(column=1, row=13)
        # Row 14
        lconfigwpa2.grid(column=0, row=14)
        self.econfigwpa2.grid(column=1, row=14)
        # Row 15
        lmental1.grid(column=0, row=15, columnspan=2)
        # Row 16
        lconfigmental1.grid(column=0, row=16)
        self.econfigmental1.grid(column=1, row=16)
        # Row 17
        lconfigmental2.grid(column=0, row=17)
        self.econfigmental2.grid(column=1, row=17)
        # Row 18
        lconfigmental3.grid(column=0, row=18)
        self.econfigmental3.grid(column=1, row=18)
        # Row 19
        lconfigmental4.grid(column=0, row=19)
        self.econfigmental4.grid(column=1, row=19)
        # Row 20
        lconfigmental5.grid(column=0, row=20)
        self.econfigmental5.grid(column=1, row=20)
        # Row 21
        lconfigmental2.grid(column=0, row=21)
        self.econfigmental2.grid(column=1, row=21)
        # Row 22
        bapply1.grid(column=0, row=22, columnspan=2)

    def createentity(self):
        # Initialize a Person Class in to self.person
        self.person = Person()
        
        # Initialize the StringVars
        self.SVname = StringVar()
        self.SVname.set(self.person.identity.name)

        # Initialize the IntVars
        
        self.personwindow()
    
    def personwindow(self, master=None):
        if master is None:
            master = self.master
        personwindow = Toplevel(master)
        personwindow.title("Person Window")
        personcontent = ttk.Frame(personwindow)
        personcontent.grid(column=0, row=0)

        # Name of Person Label
        lname = ttk.Label(personcontent, textvariable=self.SVname)

        # Physical Well Being
        # Physical Well Being Label
        lphys = ttk.Label(personcontent, text="Physical Well Being")
        
        # Physical Well Being Graph
        fphys = Figure(figsize=(5,5), dpi=100)
        a = fphys.add_subplot(111)
        # Labels for the x-axis
        physobj = ('Sickness', 'Tiredness', 'Hunger', 'Thirst')
        # Values
        physvalues = [self.person.wellbeing.physical.sick, self.person.wellbeing.physical.tired, self.person.wellbeing.physical.hunger, self.person.wellbeing.physical.thirst]
        # Create a bar chart using these values
        a.bar(physobj, physvalues, align="center")
        # Set the axis, -1 to 4 gives the x axis enough space, and -10 to 10 is the standard range for the variables
        a.axis((-1,4,0,10))

        # Mental Well Being
        # Mental Well Being Label
        lmental = ttk.Label(personcontent, text="Mental Well Being")

        # Mental Well Being Graph
        fmental = Figure(figsize=(7,5), dpi=100)
        b = fmental.add_subplot(111)
        
        # Labels for the x-axis
        mentalobj = ('Social Anxiety', 'Strength of Emotions', 'Sat w/ Self', 'Sat w/ Others', 'Sat w/ Purpose', 'Sat w/ Beliefs')
        # Values
        mentalvalues = [self.person.wellbeing.mental.socialanxiety, self.person.wellbeing.mental.strength, self.person.wellbeing.mental.satself, self.person.wellbeing.mental.satothers, self.person.wellbeing.mental.satpurp, self.person.wellbeing.mental.satspir]
        # Create a bar chart using these values
        b.bar(mentalobj, mentalvalues, align = "center", width=0.3)
        # Set the axis, -1 to 7 gives the x-axis enough space, and -10 to 10 is the standard range for the variables
        b.axis((-1, 7, 0, 10))

        # Grid
        # Row 0
        lname.grid(column=0, row=0, columnspan=2)
        # Row 1
        lphys.grid(column=0, row=1)
        lmental.grid(column=1, row=1)
        # Row 2
        cphys = FigureCanvasTkAgg(fphys, personcontent)
        cphys.get_tk_widget().grid(column=0, row=2)
        cphys.show()
        cmental = FigureCanvasTkAgg(fmental, personcontent)
        cmental.get_tk_widget().grid(column=1, row=2)
        cmental.show()


    def applychanges(self):
        # Identity Variables
        self.person.identity.name = self.econfigi1.get()


        # Emotion Variables
        self.person.emotion.valence = self.econfige1.get()
        self.person.emotion.arousal = self.econfige2.get()

        # Physical Wellbeing Variables
        self.person.wellbeing.physical.sick = self.econfigwp1.get()
        self.person.wellbeing.physical.tired = self.econfigwp2.get()
        self.person.wellbeing.physical.hunger = self.econfigwp3.get()
        self.person.wellbeing.physical.thirst = self.econfigwp4.get()

        # Physical Addiction
        self.person.wellbeing.physical.addiction.level = self.econfigwpa1.get()
        self.person.wellbeing.physical.addiction.timesince = self.econfigwpa2.get()

        # Mental Wellbeing Variables
        self.person.wellbeing.mental.socialanxiety = self.econfigmental1.get()
        self.person.wellbeing.mental.strength = self.econfigmental2.get()
        self.person.wellbeing.mental.satself = self.econfigmental3.get()
        self.person.wellbeing.mental.satothers = self.econfigmental4.get()
        self.person.wellbeing.mental.satpurp = self.econfigmental5.get()
        self.person.wellbeing.mental.satspir = self.econfigmental6.get()

        # Destory the Config Window
        self.configwindow.destroy()
        self.SVname.set(self.person.identity.name)

root = tk.Tk()
root.title("Artificial Sentient Intelligence")
app = Application(master=root)
root.mainloop()