from Dice import *

class Spell:
    def __init__(self,name,ST,PC,lvl,rnge,dur,desc):
        self.name = name
        self.saving = ST
        self.profclass = PC
        self.level = lvl
        self.range = rnge
        self.topClass = topClass
        self.duration = dur
        self.desc = desc

class Heal(Spell):
    def __init__(self, name, ST, PC, lvl, rnge, dur, effect, desc, exception=None, trgtLim=1):
        super().__init__(name, ST, PC, lvl, rnge, dur, desc)
        self.topClass = "Heal"
        self.condition = "Heal"
        self.effect = effect
        self.exception = exception
        self.targetLimit = trgtLim

    def use(self,caster,targets):
        if caster.level < self.level or caster.:
            print("You not able to use ",self.name)
        else:  
            limit = 0
            if not self.exception:
                if 'd' in self.effect:
                    effect = sum(hitRoll(self.effect))
                else: effect = int(self.effect)
                for target in targets:
                    if limit > self.targetLimit:    break
                    if target.isAlive:
                        target.condition["Heal"]=[self.dur-1,effect]
                        target.currentHealth = min(target.maxHealth,target.currentHealth+effect)
                        limit+=1
                        
            elif self.exception == "Amuse":
                for target in targets:
                    if target.isAlive:
                        target.currentHealth = min(target.maxHealth,target.currentHealth+int(target.maxHealth/2))

            elif self.exception == "Whisp":
                for target in targets:
                    if limit > self.targetLimit:    break
                    if caster.currentHealth <= int(caster.maxHealth/2):
                        print("This act can cost your life.")
                        break
                    else:
                        caster.currentHealth-=int(caster.maxHealth/2)
                        target.isAlive = True
                        target.currentHealth = 1
                        limit+=1

class Attack(Spell):
    def __init__(self, name, ST, PC, lvl, rnge, dur, desc):
        super().__init__(name, ST, PC, lvl, rnge, dur, desc)
        
spellList = {
    "Aid":Heal("Aid",None,("Cleric","Paladin"),1,3,1,"5","Choose a target around 3r and heal 5 HP."),
    "Amuse":Heal("Amuse",None,("Bard",),3,None,None,1,"Start to entertain your group, while under the influence of magic, everyone refreshes half their life. Not use in battle.","Amuse",None),
    "Heal":Heal("Heal",None,("Cleric","Druid"),2,4,1,"d8","Choose a target around 4r and roll d8 for healing."),
    "HWord":Heal("Healing Word",None,("Bard","Cleric","Druid"),1,6,1,"d4","Choose two target around 6r and roll d4",None,2),
    "LWhisp":Heal("Life Whisper",None,("Paladin",),4,1,1,"1","You can revive a recently dead target by sacrificing half of your maximum health.","Whisp"),
    "MassH":Heal("Mass Heal",None,("Cleric",),5,5,3,"d12","Create a holy aura and roll d12. For 3 turns, all campaign members will gain HP.",None,99)
}

