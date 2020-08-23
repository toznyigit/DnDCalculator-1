import random
from Dice import roll,hitRoll
from EnemyProp import randomSpecies

size = ("Tiny","Small","Medium","Large","Huge")
damageDices = ("d4","d6","d8","d10","d12")
statOrder = ("STR","DEX","CON","INT","WIS","CHA")

class Enemy:
    expList = (300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000)
    def __init__(self,species):
        self.isAlive = True
        self.stats = {"STR":0,"DEX":0,"CON":0,"INT":0,"WIS":0,"CHA":0}
        self.size = random.choice(size)
        self.name = self.size+" "+species.name
        self.level = max(species.level+size.index(self.size)-2,0)
        self.armor = sum(roll(species.race.armor))+size.index(self.size)*2
        self.condition = {}
        for order in statOrder:
            statDice = roll(str(self.level+3)+"d6")
            self.stats[order] = int(sum(sorted(statDice,reverse=True)[:3])+species.race.table[order]+(sum(roll(species.HPDice))-int(species.HPDice.split("d")[1])/2)/2)
            #self.stats[order] = max(max(roll(str(self.level+1)+species.HPDice))+species.race.table[order],0)
        self.maxHealth = sum(roll(str(self.level+1)+species.HPDice))+self.stats.get("CON","")
        self.stats["STR"] += size.index(self.size)-2
        self.stats["CON"] += size.index(self.size)-2
        self.stats["DEX"] += 2-size.index(self.size)
        self.damageDice = str(self.level+1)+damageDices[size.index(self.size)]
        self.currentHealth = self.maxHealth
        self.expReward = int(Enemy.expList[self.level]/random.randint(12,18))

    def show(self):
        if not self.isAlive:  
            return 0
        print("\n--------------------------Enemy--------------------------\n")
        print("Name: "+self.name,end =" ")
        print("\tLevel:",self.level)
        print("Health Point:",self.currentHealth,"/",self.maxHealth,"\tArmor:",self.armor,"\tHit Dice:",self.damageDice)
        for i in statOrder:
            print(i+":",str(self.stats[i]),end =" ")
        print("\n\n---------------------------------------------------------\n")

    def showHP(self):
        if not self.isAlive:  
            return 0
        print(self.name,self.currentHealth,"/",self.maxHealth)

    def attack(self,target):
        if not self.isAlive: 
            return 0

        mod = self.checkCondition(target)

        if target.condition.get("Privilege","") != "":
            if target.condition["Privilege"][0] < 0:
                print(target.name,"does not take any damage cause is under influence of aura of privilege.")
                mod*=0
        
        print(self.name,"rolls for attack '",str(self.level+1)+"d20","':",end=" ")
        atk = max(hitRoll(str(self.level+1)+"d20"))+int((self.stats["STR"]-10)/2)
        if atk >= target.armor:
            print("Damage Dice '"+self.damageDice+"':",end=" ")
            target.hurt(int(sum(hitRoll(self.damageDice))*mod))
        else:
            print("MISS!")
            return 0

    def hurt(self,damage,attacker=""):
        if not self.isAlive: 
            return 0
        self.currentHealth-=damage
        print("\n",self.name,"deal ",damage,"point")
        if self.currentHealth < 1:
            print(self.name,"is dead")
            self.isAlive = False
            if attacker.__class__.__name__ == "Player":
                attacker.gainExp(self.expReward+int(2.718**(self.level-attacker.level)))

    def checkCondition(self,target):
        atkMod = 1

        for condition in self.condition:
    
            if condition == "Charm":
                if self.condition["Charm"][0] > 0 and self.condition["Charm"][1].name == target.name:
                    print(self.name,"is charmed by",target.name)
                    self.condition["Charm"][0]-=1
                    atkMod*=0

            if condition == "Curse":
                if self.condition["Curse"][0] > 0:
                    print(self.name,"is still under the curse ande deal damage: ",end=" ")
                    self.currentHealth-=hitRoll("d6")[0]
                    print("")
                    if self.currentHealth < 0:
                        print(self.name,"died cause of the curse.")
                        return 0
                    self.condition["Curse"][0]-=1
                    atkMod*=0.5

            if condition == "DeathF":
                if self.condition["DeathF"][0] > 0:
                    self.condition["DeathF"][0]-=1
                    print(self.name,"roll for CON saving:",end=" ")
                    saving = hitRoll("d20")
                    
                    if saving[0] >= self.condition["DeathF"][2]:
                        print("SUCCESSUL 'CON' SAVING!",self.name,"is not effected from fog.")
                    else:
                        print("UNSUCCESSUL 'CON' SAVING!",self.name,"is effected from fog:",end=" ")
                        self.currentHealth-=sum(hitRoll(self.condition["DeathF"][1]))
                        print("")
                    
                    if self.currentHealth < 0:
                        print(self.name,"died cause of the fog.")
                        return 0
        
        return atkMod
