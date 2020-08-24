from Dice import *

class Spell:
    def __init__(self,name,ST,PC,lvl,rnge,dur,desc,condition):
        self.name = name
        self.saving = ST
        self.profclass = PC
        self.level = lvl
        self.range = rnge
        self.condition = condition
        self.duration = dur
        self.desc = desc

class Heal(Spell):
    def __init__(self, name, ST, PC, lvl, rnge, dur, effect, desc, exception=None, trgtLim=1, condition="Heal"):
        super().__init__(name, ST, PC, lvl, rnge, dur, desc, condition)
        self.effect = effect
        self.exception = exception
        self.targetLimit = trgtLim

    def use(self,caster,targets):
        if caster.level < self.level or caster._class not in self.profclass:
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
            else:
                for target in targets:
                    if self.exception == "Amuse" and target.isAlive:
                        target.currentHealth = min(target.maxHealth,target.currentHealth+int(target.maxHealth/2))

                    elif self.exception == "Whisp":
                        if limit > self.targetLimit or target.isAlive:    break
                        if caster.currentHealth <= int(caster.maxHealth/2):
                            print("This act can cost your life.")
                            break
                        else:
                            caster.currentHealth-=int(caster.maxHealth/2)
                            target.isAlive = True
                            target.currentHealth = 1
                            limit+=1

                    elif self.exception == "Relieve" and target.isAlive:
                        effect = sum(hitRoll(self.effect))
                        target.condition["Heal"]=[self.dur-1,effect]
                        target.currentHealth = min(target.maxHealth,target.currentHealth+effect)
                        target.condition["RC"]=[True]
                        limit+=1
                        


class Attack(Spell):
    def __init__(self, name, ST, PC, lvl, rnge, dur, effect, desc, condition, trgtLim=1):
        super().__init__(name, ST, PC, lvl, rnge, dur, desc)
        self.effect = effect
        self.targetLimit = trgtLim

    def use(self,caster,targets):
        limit = 0


        
spellList = {
    "Aid":Heal("Aid",None,("Cleric","Paladin"),1,3,1,"5","Choose a target around 3r and heal 5 HP."),
    "Amuse":Heal("Amuse",None,("Bard",),3,None,None,1,"Start to entertain your group, while under the influence of magic, everyone refreshes half their life. Not use in battle.","Amuse",None),
    "Heal":Heal("Heal",None,("Cleric","Druid"),2,4,1,"d8","Choose a target around 4r and roll d8 for healing."),
    "HWord":Heal("Healing Word",None,("Bard","Cleric","Druid"),1,6,1,"d4","Choose two target around 6r and roll d4",None,2),
    "LWhisp":Heal("Life Whisper",None,("Paladin",),4,1,1,"1","You can revive a recently dead target by sacrificing half of your maximum health.","Whisp"),
    "MassH":Heal("Mass Heal",None,("Cleric",),5,5,3,"d12","Create a holy aura and roll d12. For 3 turns, all campaign members will gain HP.",None,99),
    "Relieve":Heal("Relieve",None,("Bard","Cleric","Paladin"),4,5,1,"d10","Create a bright aura and roll d10. All campaign members will be purged of their curse and will gain HP.","Relieve",99),
    "DFog":Attack("Death Fog","CON",("Sorcerer","Wizard"),3,4,2,"4d8","Create a black fog around 4r for 2 turns. Roll 4d8 and all targets in fog will take damage.","Damage",99),
    "DHit":Attack("Death Hit",None,("Sorcerer","Warlock","Wizard"),3,2,1,"d20","Choose a target and roll d20. In case of success target disappear immideatly, otherwise you will die.","Gambling"),
    "Fireball":Attack("Fireball","DEX",("Sorcerer","Wizard"),2,8,2,"6d6","Throw a fireball around 8r and burn two targets. They will take 6d6 damage for 2 turns.","Damage",2),
    "Ignite":Attack("Ignite","CON",("Sorcerer","Warlock","Wizard"),5,6,5,"4d8","Choose a target and ignite. The target will take 4d8 damage for 5 turns."),
    "LightC":Attack("Ligthning Call","DEX",("Druid",),2,5,1,"3d10","Choose a target and roll 3d10. If target fails DEX saving, will take damage.",None),
    "LightB":Attack("Ligthning Bolt","DEX",("Sorcerer","Wizard"),2,6,1,"8d6","All target around 6r will take 6d8 damage.",None,99),
    

}

