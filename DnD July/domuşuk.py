
class Spell:
    def __init__(self,name,reqClass,reqLvl,reqComp,reqItems,targetLimit,range,effectType,effectRange,effectDice,duration,savings,offset,desc):
        self.name = name
        self.desc = desc
        self.active = False
        self.usable = True
        self.classes = reqClass
        self.reqLvl = reqLvl
        self.components = reqComp
        self.reqItems = reqItems
        self.duration = duration
        self.savings = savings
        self.currentDura = 0
        self.offset = offset
        self.effectRange = effectRange
        self.effectType = effectType
        self.effectDice = effectDice
        self.targetLimit = targetLimit

    def checkReqItems(self,player):
        for item in self.reqItems:
            itemName = item[0]
            itemCount = item[1]
            if player.inventory.bag.get(itemName,"") == "":
                return False
            if player.inventory.bag[itemName] < itemCount:
                return False
        return True

    def consumeSpell(self,player):
        if not self.active:
            if player._class.name in self.classes and self.checkReqItems(player) and player.level >= self.reqLvl and self.usable:
                print("You cast",self.name)
                self.active = True
                self.usable = False
                for item in self.reqItems:
                    player.inventory.bag[item[0]]-=item[1]
                self.currentDura = self.duration-1
                return True
            else:
                print("You not able to cast",self.name)
                return False
        else:
            if self.currentDura == 0:
                print(self.name,"is over.")
                self.active = False
                return False
            else:
                self.currentDura-=1
                return True


spells = {
    "Accuracy":Spell("Accuracy",("Ranger"),2,("V","S","M"),("Coffee Bean"),1,-1,"Boost",-1,"",2,"",{"HitDice":20},"Choose 1 target and never miss any attack during 2 round"),    
    "Aid":Spell("Aid",("Cleric","Paladin"),1,("V","S","M"),("Piece of Fabric"),2,-1,"Boost",-1,"",-8,"",{"HealthPoint":5},"Choose 2 target and boost 5 HP during 8 hours"),
    "Amuse":Spell("Amuse",("Bard"),3,("V","S"),(""),-1,-1,"Boost",-1,"",-1,"",{"HealtPoint":0.5},"Start to entertain your group, while under the influence of magic, everyone refreshes half their life. Not use in battle."),
    "Aura of Privilege":Spell("Aura of Privilege",("Cleric"),4,("V","S","M"),("Ruby","Ink"),1,-1,"Other",-1,"",-24,"",{"Condition":"No Damage"},"Choose 1 target and target will be protected from any trap or attack during 24 hours"),
    "Awaken":Spell("Awaken",("Bard","Druid"),3,("V","S","M"),("Agate Stone"),1,-1,"Summon",-1,"",-720,"",{"Servant":"Animal"},"You will affect an animal that is weaker than you that will serve you for 30 days."),
    "Bestow Curse":Spell("Bestow Curse",("Bard","Cleric","Wizard"),2,("V","S"),(""),1,-1,"Hinder",-1,"",2,"INT",{"Damage":0.5},"Choose 1 target and curse. If failure. If target fails with INT throw, will deal 1d6 damage and attack damage will be halved. during 3 round"),
    "Bless":Spell("Bless"),
    "Blindness/Deafness":Spell("Blindness/Deafness"),
    "Clone":Spell("Clone"),
    "Charm":Spell("Bless"),
    "Death Cloud":Spell("Death Cloud"),
    "Death Slap":Spell("Death Slap"),
    "Death Ward":Spell("Death Ward"),
    "Decoy":Spell("Decoy"),
    "Defence Breaker":Spell("Defence Breaker"),
    "Defraud":Spell("Defraud"),
    "Dimension Door":Spell("Dimension Door"),
    "Disguise":Spell("Disguise"),
    "Dissonant Whisper":Spell("Dissonant Whisper"),
    "Domination":Spell("Domination"),
    "Encouragement":Spell("Encouragement"),
    "Enthrall":Spell("Enthrall"),
    "Feign Death":Spell("Feign Death"),
    "Fart":Spell("Fart"),
    "Fear":Spell("Fear"),
    "Fireball":Spell("Fireball"),
    "Fog":Spell("Fog"),
    "Foresight":Spell("Foresight"),
    "Forethought":Spell("Forethought"),
    "Heal":Spell("Heal"),
    "Healing Word":Spell("Healing Word"),
    "Ignite":Spell("Ignite"),
    "Intuition":Spell("Intuition"),
    "Invisible":Spell("Invisible"),
    "Levitate":Spell("Levitate"),
    "Life Whisper":Spell("Life Whisper"),
    "Lightning Call":Spell("Lightning Call"),
    "Lightning Bolt":Spell("Lightning Bolt"),
    "Magic Wall":Spell("Magic Wall"),
    "Magical Missile":Spell("Magical Missile"),
    "Mass Heal":Spell("Mass Heal"),
    "Pathfinder":Spell("Pathfinder"),
    "Poison Ivy":Spell("Poison Ivy"),
    "Relieve":Spell("Relieve"),
    "Remove Curse":Spell("Remove Curse"),
    "Shield":Spell("Shield"),
    "Sleep":Spell("Sleep"),
    "Spectral Mark":Spell("Spectral Mark"),
    "Stall":Spell("Stall"),
    "Stone Rain":Spell("Stone Rain"),
    "Stun":Spell("Stun"),
    "Summon":Spell("Summon"),
    "Swift Quiver":Spell("Swift Quiver"),
    "Telekinesis":Spell("Telekinesis"),
    "Teleport":Spell("Teleport"),    
    "Tergiversation":Spell("Tergiversation"),
    "Thorn":Spell("Thorn"),
    "Truth":Spell("Truth",("Paladin"),3,("V","S"),(""),1,-1,"Other",),
    "Vampire Breath":Spell("Vampire Breath"),
    "Vanish":Spell("Vanish",("Warlock","Wizard"),3,("V","S"),(""),1,-1,"Action",-1,1,"",{},"d20","Choose a target whose level will be less than your level and roll the d20. If you succeed, you will vanish the target. If you fail, you will take as much damage as the target's current health."),
    "Vortex":Spell("Vortex",("Wizard"),3,("V","S"),(""),-1,10,"Action",6,"",-1,"STR",{},"Choose a point up to a distance of 10d, and everyone 6d in diameter drags there.")    
}