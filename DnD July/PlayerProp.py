statList = {"STR":0,"DEX":0,"CON":0,"INT":0,"WIS":0,"CHA":0}
statOrder = ("STR","DEX","CON","INT","WIS","CHA")

class Skill:
    def __init__(self,name,ability,proficiency):
        self.name = name
        self.ability = ability
        self.proficiency = proficiency
        self.point = 0
    def setPoint(self):
        self.point = (self.ability-10)/2+self.proficiency

skillList = {
    "Athletics":Skill("Athletics","STR",0),
    "Acrobatics":Skill("Acrobatics","DEX",0),
    "Sleight":Skill("Sleight of Hands","DEX",0),
    "Stealth":Skill("Stealth","DEX",0),
    "Arcana":Skill("Arcana","INT",0),
    "History":Skill("History","INT",0),
    "Invest":Skill("Investigation","INT",0),
    "Nature":Skill("Nature","INT",0),
    "Religion":Skill("Religion","INT",0),
    "Handling":Skill("Animal Handling","WIS",0),
    "Insight":Skill("Insight","WIS",0),
    "Medicine":Skill("Medicine","WIS",0),
    "Perception":Skill("Perception","WIS",0),
    "Survival":Skill("Survival","WIS",0),
    "Deception":Skill("Deception","CHA",0),
    "Intimidation":Skill("Intimidation","CHA",0),
    "Performance":Skill("Performance","CHA",0),
    "Persuasion":Skill("Persuasion","CHA",0)
}


class Class:
    skillOrder = ("Athletics",
            "Acrobatics","Sleight","Stealth",
            "Arcana","History","Invest","Nature","Religion",
            "Handling","Insight","Medicine","Perception","Survival",
            "Deception","Intimidation","Performance","Persuasion")

    def __init__(self,name,damage,health,savings,skills,special):
        self.name = name
        self.damage = damage
        self.health = health[0]
        self.healthIncr = health[1]
        self.savings = savings
        self.skills = skills[1]
        self.skillCount = skills[0]
        self.special = special

    def isAvailable(self,skill):
        if -1 in self.skills: return True
        if Class.skillOrder.index(skill) in self.skills: return True
        else: return False

    def printAvailable(self):
        print(self.name+" can choose '"+str(self.skillCount)+"' skills from available: ")
        for item in Class.skillOrder:
            flag = self.isAvailable(item)
            if self.skills.__contains__(-1):
                flag = True
            if flag: print(item)

classList = {
    "Barbarian":Class("Barbarian","d12",(12,7),("STR","CON"),(2,(0,7,9,12,13,15)),"Rage"),
    "Bard":Class("Bard","d8",(8,5),("DEX","CHA"),(3,(-1,0)),"Diversion"),
    "Cleric":Class("Cleric","d8",(8,5),("WIS","CHA"),(2,(5,8,10,11,17)),"Healing"),
    "Druid":Class("Druid","d8",(8,5),("WIS","INT"),(2,(4,7,8,9,10,11,12,13)),"Whisper"),
    "Fighter":Class("Fighter","d10",(10,6),("STR","CON"),(2,(0,1,5,9,10,12,13,15)),"Second Wind"),
    "Monk":Class("Bard","d8",(8,5),("DEX","STR"),(2,(0,1,3,5,8,10)),"Martial Art"),
    "Paladin":Class("Paladin","d10",(10,6),("WIS","CHA"),(2,(0,8,10,11,15,17)),"Divine Sense"),
    "Ranger":Class("Ranger","d10",(10,6),("STR","DEX"),(3,(0,3,6,7,9,10,12,13)),"Natural Explorer"),
    "Rouge":Class("Rouge","d8",(8,5),("INT","DEX"),(4,(0,1,2,3,6,10,12,14,15,16,17)),"Infiltrate"),
    "Sorcerer":Class("Sorcerer","d6",(6,4),("CON","CHA"),(2,(4,8,10,14,15,17)),"Metamagic"),
    "Warlock":Class("Warlock","d8",(8,5),("WIS","CHA"),(2,(4,5,6,7,8,14,15)),"Summoner"),
    "Wizard":Class("Rouge","d6",(6,4),("INT","WIS"),(2,(4,5,6,8,10,11)),"Spellcasting")   
}

class Races:
    def __init__(self,name,status,passive):
        self.name = name
        self.status = status
        self.passive = passive

races = {
    "Dragonborn":Races("Dragonborn",(2,-1,0,0,0,1),"With your breath, a selected enemy can be put to sleep."),
    "Dwarf":Races("Dwarf",(1,0,2,0,0,-1),"You can see in darkness, but in shades of gray."),
    "Elf":Races("Elf",(0,2,-1,0,0,1),"You not need sleep, you can renew yourself with trans."),
    "Gnome":Races("Gnome",(0,0,0,2,0,0),"Your small body provides stealthiness."),
    "Halfelf":Races("Half-Elf",(-1,1,0,0,0,2),"With your words, enemies can be influenced."),
    "Halfling":Races("Halfling",(-1,2,0,0,0,1),"With your luck, you can roll a second dice. Remember only last dice is valid."),
    "Halforc":Races("Half-Orc",(1,0,2,0,0,-1),"Orc blood makes you more enduring."),
    "Human":Races("Human",(1,1,1,1,1,1),"You are just a human."),
    "Tiefling":Races("Tiefling",(0,1,0,2,1,-2),"You scare everyone with your appearance.")    
}