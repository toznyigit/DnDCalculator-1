from PlayerProp import *
from Dice import *
from Inventory import *

def Death(obj):
    del obj

class Player:
    expList = [300,900,2700,6500,14000,23000,34000,48000,64000,1000000000]
    def __init__(self,name,_class,_race,_preferred,exp = 0):
        self.isAlive = True
        self.name = name
        self.inventory = kits[_class]
        self.condition = {}
        self.skills = skillList
        self.stats = statList
        self._class = classList.get(_class,"")
        self._race = races.get(_race,"")
        self.exp = exp
        self.level = 1
        self.compSkills = []
        self.servant = {}
        self.currentHealth = self.maxHealth()
        self.armor = self.inventory.armor.protect
        i = 0
        for skill in _preferred:
            if i == self._class.skillCount: break
            if self._class.isAvailable(skill): self.compSkills.append(skill)
            i+=1
        j = 0
        for stats in statOrder:
            print("Roll for",stats,end =": ")
            statDice = hitRoll("4d6")
            print("")
            self.stats[stats] = sum(statDice)-min(statDice)+self._race.status[j]
            j+=1
        for skill in Class.skillOrder:
            self.skills[skill].point = int((self.stats[self.skills[skill].ability]-10)/2)
            if skill in self.compSkills: self.skills[skill].point+=self.proficiency
        self.currentBackpack = 5+int((self.stats["CON"]-10)/2)
        for item in self.inventory.backpack:
            if weapons.get(item,"") != "":
                self.currentBackpack -= self.inventory.backpack[item].size
        self.currentPouch = 20+5*int((self.stats["CON"]-10)/2)
        for item in self.inventory.pouch:
            self.currentPouch -= self.inventory.pouch[item]

    def gainExp(self,rewardExp):
        if not self.isAlive: 
            print("Death character can not gain exp.") 
            return
        self.exp+=rewardExp
        while self.exp > Player.expList[self.level]:
            self.level+=1
            for skill in self.compSkills:
                self.skills[skill].point+=self.proficiency
            self.currentHealth = self.maxHealth()

    def buy(self,item,count=1):
        if not self.isAlive: 
            print("Death character can not buy.") 
            return
        if item in armors:
            print("Armor trading not available for now.")
        if item in potions:
            item = potions[item]
            if self.inventory.coin < item.price*count:
                count = int(self.inventory.coin/item.price)
                print("You can not buy more than",count,item.name,"Potion")
            if item.name in self.inventory.sack:
                self.inventory.sack[item.name][1] += count
            else:
                self.inventory.sack[item.name] = [item,count,0]
            self.inventory.coin -= item.price*count
        else:
            item = weapons[item]
            if item.__class__.__name__ == "Throw":
                if self.currentBackpack < item.size:
                    print("No slot in inventory for",item.name)
                    return
                if self.inventory.coin < item.price*count:
                    count = int(self.inventory.coin/item.price)
                    print("You can not buy more than",count,item.name)
                if self.inventory.coin >= item.price*count:
                    self.inventory.coin -= item.price*count
                    self.inventory.backpack[item.name] = item
                    self.currentBackpack-=item.size
                    self.inventory.backpack[item.name].change(1,count)
                else:
                    print("Not enough money for",item.name)
                    return
            elif item.__class__.__name__ == "Ammo":
                if self.currentPouch < count:
                    count = self.currentPouch
                    if self.inventory.coin < item.price*count:
                        count = int(self.inventory.coin/item.price)
                    print("You can not buy more than",count,item.name)
                if self.inventory.coin >= item.price*count:
                    self.inventory.coin -= item.price*count
                    self.inventory.pouch[item.name] = count
                    self.currentPouch-=count
                else:
                    print("Not enough money for",item.name)
                    return
            else:
                if self.currentBackpack < item.size:
                    print("No slot in inventory for",item.name)
                    return
                else:
                    if self.inventory.coin >= item.price:
                        self.inventory.coin -= item.price
                        self.inventory.backpack[item.name] = item
                        self.currentBackpack-=item.size
                    else:
                        print("Not enough money for",item.name)
                        return
        print("You buy",count,item.name,end="\n")

    def sell(self,item,count=1):
        flag = False
        if not self.isAlive: 
            print("Death character can not sell.")
            return
        if self.inventory.backpack.get(item,"") != "":
            if weapons[item].__class__.__name__ == "Throw":
                if self.inventory.backpack[item].piece < count:
                    count = self.inventory.pouch[item].piece 
                    print("You can not sell more than",count,item)
            self.inventory.coin += int(weapons[item].price/5)*count
            self.inventory.backpack[item].change(-1,count)
            if  self.inventory.backpack[item].piece == 0:
                self.currentBackpack += weapons[item].size
                del self.inventory.backpack[item]
            flag = True
        if self.inventory.pouch.get(item,"") != "":
            if self.inventory.pouch[item] < count:
                count = self.inventory.pouch[item]
                print("You can not sell more than",count,item)
            self.inventory.coin += int(ammos[item].price/5)*count
            self.currentPouch += count
            self.inventory.pouch[item] -= count
            flag = True
        if self.inventory.sack.get(item,"") != "":
            if self.inventory.sack[item][1] < count:
                count = self.inventory.sack[item][1]
                print("You can not sell more than",count,item)
            self.inventory.coin += int(potions[item].price/5)*count
            self.inventory.sack[item][1] -= count
            flag = True

        if flag is True: print("You sell",count,item,end="\n")


    def loot(self,item,count=1):
        if not self.isAlive: 
            print("Death character can not loot.") 
            return
        if item in potions:
            item = potions[item]
            if item.name in self.inventory.sack:
                self.inventory.sack[item.name][1] += count
            else:
                self.inventory.sack[item.name] = [item,count,0]
        else:
            if weapons[item].__class__.__name__ == "Ammo":
                if self.inventory.pouchSlot < count:
                    count = self.inventory.pouchSlot
                    print("You can not loot more than",count,weapons[item].name)
                self.inventory.pouch[item] = count
                self.inventory.pouchSlot-= count
            else:
                if self.inventory.backpackSlot < weapons[item].size:
                    print("No slot in inventory for",item.name)
                else:
                    self.inventory.backpack[item] = weapons[item]
                    self.inventory.backpackSlot-= weapons[item].size

    def attack(self,item,target,distance):
        if not self.isAlive: 
            print("Death character can not attack.") 
            return
        className = self.inventory.backpack[item].__class__.__name__

        for condition in self.condition:

            if condition == "Clone":
                continue
            if self.condition[condition][0] > 0:
                self.condition[condition][0]-=1

        if self.inventory.backpack.get(item,"") == "":
            print("No",item,"in inventory, choose another weapon.")
            return 0
        if className == "Ranged":
            atkMod = self.consumePotion("Speed")+int((self.stats["DEX"]-10)/2)
            ammo = self.inventory.backpack[item].ammo.name
            if self.inventory.pouch.get(ammo,"") == "":
                print("No",ammo,"left, attack is missed.")
                return 0
            elif self.inventory.pouch[ammo] < 1:
                print("No",ammo,"left, attack is missed.")
                return 0
        elif className == "Throw":
            atkMod = self.consumePotion("Speed")+int((self.stats["DEX"]-10)/2)
            if self.inventory.backpack.get(item,"") == "":
                print("No",item,"left, attack is missed.")
                return 0
            if self.inventory.backpack[item].piece < 0:
                print("No",item,"left, attack is missed.")
                return 0
        elif className == "Melee":
            atkMod = self.consumePotion("Battle")+int((self.stats["STR"]-10)/2)
        
        if weapons[item].range < distance:
                print("\nTarget is out of range, attack is missed")
                return 0
        if className == "Ranged" and distance < 4:
                print("\nTarget is too close for a ranged weapon, attack is missed")
                return 0
        
        print(self.name,"rolls for attack 'd20':",end=" ")
        attack = hitRoll("d20")[0]
        if self.condition.get("Attack","") != "":
            if self.condition["Attack"][0] >= 0:
                print("Accuracy is active.")
                attack = 30
        
        if self.condition.get("Defense","") != "":
            print("Defense Breaker is active.")
            attack = 30

        if attack==1 or attack+atkMod < target.armor:
            print("MISS")
            return 0
        
        print("Damage Dice '"+str(self.level)+weapons[item].dice+"':",end=" ")
        if className == "Ranged":
            self.inventory.pouch[self.inventory.backpack[item].ammo.name]-=1                
        elif className == "Throw":
            self.inventory.backpack[item].change(-1,1)
        target.hurt(sum(hitRoll(str(self.level)+weapons[item].dice))+atkMod,self)

    def usePotion(self,potion):
        if not self.isAlive: 
            print("Character is dead.") 
            return
        if potion not in self.inventory.sack or self.inventory.sack[potion][1] == 0:
            print("0",potion,"potion in inventory")
            return
        print(self.name,"use",potion,"potion")
        self.inventory.sack[potion][1]-=1
        self.inventory.sack[potion][2] = potions[potion].duration
        if potion == "Health":
            self.currentHealth = min(self.currentHealth+self._class.healthIncr,self.maxHealth())


    def consumePotion(self,potion):
        if not self.isAlive: 
            print("Death character can not use potion.") 
            return
        if self.inventory.sack.get(potion,"") != "":
            self.inventory.sack[potion][2]-=1
            return 2
        else: return 0
        
    def hurt(self,damage):
        if not self.isAlive: 
            print("Character is dead.") 
            return
        self.currentHealth-=damage
        print("\n",self.name,"deal ",damage,"point")
        if self.currentHealth < 1:
            if self.condition.get("DeathW","") != "":
                if self.condition["DeathW"][0] < 0:
                    print(self.name,"protect from death.")
                    self.condition["DeathW"][0] = 0
                    self.currentHealth = 1
                    return
            print(self.name,"is dead")
            self.isAlive = False

    def show(self):
        if not self.isAlive: 
            print("Death character can not show yourself.") 
            return
        print("\n--------------------------Character--------------------------\n")
        print("Name:"+self.name,"\t",self._race.name,self._class.name,"\tLevel:",self.level,"(",self.exp,"/",Player.expList[self.level],")")
        print()
        print("Health Point:",self.currentHealth,"/",self.maxHealth(),"\tArmor:",self.armor)
        print()
        for i in statOrder:
            print(i+":",str(self.stats[i]),end =" ")
        print("\n")
        for j in Class.skillOrder:
            if j in self.compSkills:    print("[X] ",end="")
            else:   print("[ ] ",end="")
            print(self.skills[j].name+":",self.skills[j].point)
        print("\nBackpack:",self.currentBackpack,"/",5+int((self.stats["CON"]-10)/2),"\tPouch:",self.currentPouch,"/",20+5*int((self.stats["CON"]-10)/2))
        self.inventory.show()

    def showHP(self):
        if not self.isAlive: 
            print("Death character can not be hurted.") 
            return
        print(self.name,self.currentHealth,"/",self.maxHealth())
        
    @property
    def proficiency(self):
        return (int(self.level/3)+2)
    def maxHealth(self):
        health = 0
        if self.condition.get("Health","") != "":
            if self.condition["Health"][0] != 0:
                health+= 5
        health += (self._class.health+(self._class.healthIncr)*self.level)
        return int(health)
    def carry(self):
        return self.stats["CON"]
        
# Dick = Player("Dick","Barbarian","Human",("Athletics","Stealth"))

# Dick.show()
# for i in range(4):
#     print("\nShoot:",Dick.attack("Axe",0,1),"\n")


# Dick.buy("Dick",2)
# Dick.buy("Dick",2)
# print(Dick.inventory.sack["Dick"])
# Dick.usePotion("Dick")
# print(Dick.inventory.sack["Dick"])

# Dick.buy("Sling")
# Dick.buy("Short Bow")
# Dick.buy("Greatsword")
# Dick.buy("Falx")
# Dick.buy("Crossbow")
# Dick.buy("Arrow",3)

# Dick.sell("Arrow",3)
# Dick.sell("Arrow",1)
# Dick.sell("Dick",3)
# Dick.sell("Dick",1)
# Dick.sell("Short Bow")
# Dick.buy("Short Bow")
# print(Dick.inventory.backpack["Bow"].price)
# print(Dick.inventory.pouch["Arrow"])

# Dick.attack("Short Bow",0)
# Dick.attack("Short Bow",0)
# print(Dick.inventory.sack["Dick"])
# Dick.attack("Short Bow",0)
# print(Dick.inventory.sack["Dick"])

# Dick.buy("Health",2)
# Dick.show()
# time.sleep(1)
# Dick.hurt(9)
# print(Dick.name,"'s HP: ",Dick.currentHealth,"/",Dick.maxHealth())
# time.sleep(1)
# Dick.usePotion("Health")
# time.sleep(1)
# print(Dick.name,"'s HP: ",Dick.currentHealth,"/",Dick.maxHealth())
# time.sleep(1)
# Dick.hurt(16)
# print(Dick.name,"'s HP: ",Dick.currentHealth,"/",Dick.maxHealth())
# time.sleep(1)
# Dick.hurt(3)