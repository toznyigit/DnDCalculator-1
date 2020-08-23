from Enemy import *
from Dice import *
import time,copy

class Spell:
    def __init__(self,Name,Class,Level,Distance,Range,Target,Components,Desc):
        self.name = Name
        self.desc = Desc
        self._class = Class
        self.level = Level
        self.distance = Distance
        self.range = Range
        self.target = Target
        self.components = Components

    def show(self):
        print("\n\n--------------------------Spell--------------------------\n")
        print("Spell Name:",self.name)
        print("Spell Description:",self.desc)
        print("Requirements:")
        print("\tClass:",end=" ")
        for i in self._class:
            print(i,end=" ")
        print("\n\tLevel:",self.level)
        print("\tComponents:",end=" ")
        for i in self.components:
            if i.__class__.__name__ == "tuple":
                print(i[0],end=": ")
                for j in range(1,len(i)):
                    print(i[j],end=", ")
            else: print(i,end=", ")


        print("\n---------------------------------------------------------\n")

class Accuracy(Spell):
    def __init__(self):
        super().__init__("Accuracy",("Ranger",),2,0,0,1,("V","S",("M","Coffee Bean")),"With effect of spell, you won't miss hits during 2 turns.")

    def use(self,target):
        target.condition["Attack"] = [2]

class Aid(Spell):
    def __init__(self):
        super().__init__("Aid",("Cleric","Paladin",),1,0,0,2,("V","S",("M","Cloth Piece")),"Choose 2 targets and they gain 5 HP for 24 hours.")

    def use(self,targets):
        for i in range(2):
            target = targets[i]
            target.condition["Health"] = [-24]

class Amuse(Spell):
    def __init__(self):
        super().__init__("Amuse",("Bard",),3,0,0,-1,("V","S"),"Start to entertain your group, while under the influence of magic, everyone refreshes half their life. Not use in battle.")
    
    def use(self,targets):
        for target in targets:
            target.currentHealth=min(target.currentHealth+int(target.maxHealth()/2),target.maxHealth())

class Aura(Spell):
    def __init__(self):
        super().__init__("Aura of Privilege",("Cleric",),1,0,0,2,("V","S",("M","Ruby","Ink")),"Choose a target and target will be protected from any trap or attack during 24 hours.")

    def use(self,targets):
        for target in targets:
            target.condition["Privilege"] = [-24]

class Awaken(Spell):
    def __init__(self):
        super().__init__("Awaken",("Bard","Druid",),3,0,0,1,("V","S",("M","Agate Stone")),"You will affect an animal that is weaker than you that will serve you for 30 days.")

    def use(self,target):
        while True:
            victim = Enemy(randomSpecies(target.level))
            if victim.level < target.level:
                print("You captivated a",victim.name)
                key = input("Give your servant a name: ")
                victim.name = key+" ("+victim.name+")"
                break
        target.servant[key] = victim

class Bestow(Spell):
    def __init__(self):
        super().__init__("Bestow Curse",("Bard","Cleric","Wizard",),2,0,0,1,("V","S"),"Choose a target and curse. If target fails with INT throw, will deal 1d6 damage and attack damage will be halved, during 3 rounds.")

    def use(self,target,savingLimit=0):
        print(target.name,"roll for INT saving:",end=" ")
        saving = hitRoll("d20")
        if saving[0] >= savingLimit:
            print("SUCCESSUL 'INT' SAVING!",target.name,"is not cursed.")
        else:
            print("UNSUCCESSUL 'INT' SAVING!",target.name,"is cursed.")
            target.condition["Curse"] = [3]

class Bless(Spell):
    def __init__(self):
        super().__init__("Bless",("Cleric","Paladin",),1,0,0,2,("V","S",("M","Holy Water")),"Choose 2 targets and bless them. When they roll savings, they also roll an extra 'd4' and add actual result, during 3 rounds.")

    def use(self,target):
        target.condition["Saving"] = [3,"d4"]
        # Player a saving kısmı eklenecek

class BlindDeaf(Spell):
    def __init__(self):
        super().__init__("Blindness/Deafness",("Bard","Cleric","Sorcerer","Wizard"),1,0,0,1,("V"),"Choose a target and choose blindness or deafness. If target fails with CON throw, target is deaf or blind during 3 turns.")

    def use(self,target,savingLimit=0):
        pass
        # büyü kullanabilen düşmanlar eklendikten sonra düzenlenecek
    
class Clone(Spell):
    def __init__(self):
        super().__init__("Clone",("Wizard",),4,0,0,1,("V","S",("M","Target's Blood","Target's Meat")),"Choose a player and clone. During cloning you need blood and meat. This will cause half of the player's health so be careful. Clone will vanish end of battle.")

    def use(self,target):
        fakePlayer = copy.deepcopy(target)
        fakePlayer.condition["Clone"] = True
        fakePlayer.name = "Clone "+fakePlayer.name
        return fakePlayer
    
    def destroyClone(self,target):
        if target.condition.get("Clone","") != "":
            del target
        else:
            print(target.name,"is real, not a clone.")

class Charm(Spell):
    def __init__(self):
        super().__init__("Charm",("Bard","Druid","Sorcerer","Wizard"),3,0,0,1,("V","S"),"Choose a target and charm. If target fails with CHA throw, target not attack spellcaster during 3 turns.")

    def use(self,target,caster,savingLimit=0):
        print(target.name,"roll for CHA saving:",end=" ")
        saving = hitRoll("d20")
        if saving[0] >= savingLimit:
            print("SUCCESSUL 'CHA' SAVING!",target.name,"is not charmed.")
        else:
            print("UNSUCCESSUL 'CHA' SAVING!",target.name,"is charmed.")
            target.condition["Charm"] = [3,caster]

class DeathF(Spell):
    def __init__(self):
        super().__init__("Death Fog",("Sorcerer","Wizard"),3,8,4,-1,("V","S"),"Create a fog radiating in 4d. All targets in fog, roll CON throw and if fail take 2d8 damage.")
    
    def use(self,targets,savingLimit=0):
        for target in targets:
            target.condition["DeathF"] = [3,"2d8",savingLimit]      

class DeathH(Spell):
    def __init__(self):
        super().__init__("Death Hit",("Sorcerer","Warlock","Wizard"),3,0,0,1,("V","S",("M","Mushroom Worm")),"If you success d20 roll, target will die immediately, else you'll die.")

    def use(self,target,caster,savingLimit=0):
        print(caster.name,"roll for d20:",end=" ")
        saving = hitRoll("d20")
        if saving[0] >= savingLimit:
            print("SUCCESSUL ROLL!",target.name,"is killed by Death Hit")
            target.currentHealth = 0
            target.isAlive = False
        else:
            print("UNSUCCESSUL ROLL!",caster.name,"died because of stupidity.")
            caster.currentHealth = 0
            caster.isAlive = False

class DeathW(Spell):
    def __init__(self):
        super().__init__("Death Ward",("Cleric","Paladin"),2,0,0,1,("V","S"),"Choose a target and protect from death. During 8 hours, if target's HP drops 0, target won't die and the HP increase 1.")
    
    def use(self,target):
        target.condition["DeathW"] = [-8]
# class Decoy(Spell):
class Defense(Spell):
    def __init__(self):
        super().__init__("Defense Breaker", ("Bard","Cleric","Paladin","Sorcerer","Wizard"),5,0,0,1,("V","S",("M","Aqua Regia")),"For 8 hours, enemies lose their shield who will be attacked by you.")
    def use(self,caster):
        target.condition["Defense"] = [-8]
# class Defraud(Spell):
# class Dimension(Spell):
# class Disguise(Spell):
# class Dissonant(Spell):
# class Domination(Spell):
# class Encouragement(Spell):
# class Enthrall(Spell):
# class Feign(Spell):
# class Fart(Spell):
# class Fear(Spell):
# class Fireball(Spell):
# class Fog(Spell):
# class Foresight(Spell):
# class Forethought(Spell):
# class HealN(Spell):
# class HealW(Spell):
# class Ignite(Spell):
# class Intuition(Spell):
# class Invisible(Spell):
# class Levitate(Spell):
# class LifeW(Spell):
# class LightningB(Spell):
# class LightningC(Spell):
# class MagicW(Spell):
# class MagicM(Spell):
# class Mass(Spell):
# class Pathfinder(Spell):
# class Poison(Spell):
# class Relieve(Spell):
# class Remove(Spell):
# class Shield(Spell):
# class Side(Spell):
# class Sleep(Spell):
# class Spectral(Spell):
# class Stall(Spell):
# class Stone(Spell):
# class Stun(Spell):
# class Summon(Spell):
# class Swift(Spell):
# class Telekinesis(Spell):
# class Teleport(Spell):
# class Thorn(Spell):
# class Truth(Spell):
# class Vampire(Spell):
# class Vanish(Spell):
# class Vortex(Spell):
