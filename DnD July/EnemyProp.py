import random
from Dice import roll
statOrder = ("STR","DEX","CON","INT","WIS","CHA")

class Races:
    def __init__(self,name,status,armor):
        self.table = {"STR":0,"DEX":0,"CON":0,"INT":0,"WIS":0,"CHA":0}
        i = 0
        self.name = name
        for stats in statOrder:
            self.table[stats] = status[i]
            i+=1
        self.armor = armor

races  = {
    "Animal":Races("Animal",(1,3,-1,-1,0,-1),"1d12"),
    "Creature":Races("Creature",(1,2,1,-2,-1,-2),"2d8"),
    "Undead":Races("Undead",(1,-1,3,-2,-1,-1),"1d20"),
    "Beast":Races("Beast",(4,-3,3,2,-1,2),"2d12"),
    "Humanoid":Races("Humanoid",(1,1,1,1,1,2),"3d6")
}
    
class Species:
    def __init__(self,name,race,level,HPDice):
        self.name = name
        self.race = races.get(race,"")
        self.level = level
        self.HPDice = HPDice

species = {
    "Bee":Species("Bee","Animal",0,"d4"),
    "Bat":Species("Bat","Animal",0,"d4"),
    "Slime":Species("Slime","Creature",0,"d4"),
    "Worm":Species("Worm","Animal",0,"d4"),
    "Spider":Species("Spider","Animal",1,"d6"),
    "Rat":Species("Rat","Animal",1,"d6"),
    "Raven":Species("Raven","Animal",1,"d6"),
    "Hornet":Species("Hornet","Animal",1,"d6"),
    "Snake":Species("Snake","Animal",2,"d8"),
    "Skull":Species("Skull","Creature",2,"d8"),
    "Mimic":Species("Mimic","Creature",2,"d8"),
    "Pixie":Species("Pixie","Creature",2,"d8"),
    "Goblin":Species("Goblin","Humanoid",3,"d10"),
    "Zombie":Species("Zombie","Undead",3,"d10"),
    "Skeleton":Species("Skeleton","Undead",3,"d10"),
    "Thief":Species("Thief","Humanoid",3,"d10"),
    "Wolf":Species("Wolf","Animal",4,"d10"),
    "Jester":Species("Jester","Humanoid",4,"d10"),
    "Bandit":Species("Bandit","Humanoid",4,"d10"),
    "Commander":Species("Commander","Humanoid",4,"d10"),
    "Mummy":Species("Mummy","Undead",5,"d12"),
    "Cultist":Species("Cultist","Humanoid",5,"d12"),
    "Ghost":Species("Ghost","Undead",5,"d12"),
    "Ghoul":Species("Ghoul","Creature",5,"d12"),
    "Werewolf":Species("Werewolf","Beast",6,"d20"),
    "Wraith":Species("Wraith","Undead",6,"d20"),
    "Golem":Species("Golem","Beast",6,"d20"),
    "Wyvern":Species("Wyvern","Beast",6,"d20"),
    "Necromencer":Species("Necromencer","Humanoid",7,"d20"),
    "Elemental":Species("Elemental","Beast",7,"d20"),
    "Mage":Species("Mage","Humanoid",7,"d20"),
    "Dragon":Species("Dragon","Beast",8,"d20"),
    "Chief":Species("Chief","Humanoid",8,"d20"),
    "Lord":Species("The Lord","Humanoid",8,"d20")
}

def returnSpecies(kind):
    return species.get(kind,"")

def returnRace(race):
    return races.get(race,"")

def randomSpecies(level=11):
    while True:
        enemy = species.get(random.choice(list(species.keys())),"")
        if enemy.level <= level-1: return enemy 
    