from Inventory import *
from Player import *

class Action(Player):
    def gainExp(self,rewardExp):
        self.exp+=rewardExp
        if self.exp > Player.expList[self.level]:
            self.level+=1
            for skill in self.compSkills:
                self.skills[skill].point+=self.proficiency

    def buy(self,item,count=1):
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
            if weapons[item].__class__.__name__ == "Ammo":
                if self.inventory.pouchSlot < count:
                    count = self.inventory.pouchSlot
                    if self.inventory.coin < weapons[item].price*count:
                        count = int(self.inventory.coin/weapons[item].price)
                    print("You can not buy more than",count,weapons[item].name)
                if self.inventory.coin >= weapons[item].price*count:
                    self.inventory.coin -= weapons[item].price*count
                    self.inventory.pouch[item] = count
                    self.inventory.pouchSlot-= count
                else:
                    print("Not enough money")
            else:
                if self.inventory.backpackSlot < weapons[item].size:
                    print("No slot in inventory.")
                else:
                    if self.inventory.coin >= weapons[item].price:
                        self.inventory.coin -= weapons[item].price
                        self.inventory.backpack[item] = weapons[item]
                        self.inventory.backpackSlot-= weapons[item].size
                    else:
                        print("Not enough money.")
                        
    def attack(self,item):
        if self.inventory.backpack[item].__class__.__name__ == "Ranged":
            if self.inventory.backpack[item].ammo.name in self.inventory.pouch and self.inventory.pouch[self.inventory.backpack[item].ammo.name]:
                self.inventory.pouch[self.inventory.backpack[item].ammo.name]-=1
                self.inventory.sack["Dick"][2]-=1
            else:
                print("No",self.inventory.backpack[item].ammo.name,"left, choose another weapon.")
                self.attack(input())

    def usePotion(self,potion):
        if potion not in self.inventory.sack or self.inventory.sack[potion][1] == 0:
            print("0",potion,"potion in inventory")
            return
        print(self.inventory.sack[potion][1])
        self.inventory.sack[potion][1]-=1
        self.inventory.sack[potion][2] = potions[potion].duration
        


    def show(self):
        print("")
        print("----------------------------------------------------------------------")
        print("")
        print("Name: "+self.name,"\t",self._race.name,self._class.name,"\tLevel: ",self.level)
        #print("Armor: "+str(self.armor))
        print("Health Point: ",self.maxHealth(),end =" ")
        print("\tHit Dice: "+self._class.hit)
        for i in statOrder:
            print(i+": "+str(self.stats[i]),end =" ")
        print("")
        for j in Class.skillOrder:
            if j in self.compSkills:
                print("[X]",end="")
            print(self.skills[j].name,": ",self.skills[j].point,end =" ")
        print("")
        print("")
        print("----------------------------------------------------------------------")
        print("")