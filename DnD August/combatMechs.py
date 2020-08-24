from Inventory import *
from Dice import *
from condMechs import *

def attack(obj,item,target,distance):
        if not obj.isAlive: 
            print("Death character can not attack.") 
            return
        className = obj.inventory.backpack[item].__class__.__name__

        if obj.inventory.backpack.get(item,"") == "":
            print("No",item,"in inventory, choose another weapon.")
            return 0
        if className == "Ranged":
            atkMod = obj.consumePotion("Speed")+int((obj.stats["DEX"]-10)/2)
            ammo = obj.inventory.backpack[item].ammo.name
            if obj.inventory.pouch.get(ammo,"") == "":
                print("No",ammo,"left, attack is missed.")
                return 0
            elif obj.inventory.pouch[ammo] < 1:
                print("No",ammo,"left, attack is missed.")
                return 0
        elif className == "Throw":
            atkMod = obj.consumePotion("Speed")+int((obj.stats["DEX"]-10)/2)
            if obj.inventory.backpack.get(item,"") == "":
                print("No",item,"left, attack is missed.")
                return 0
            if obj.inventory.backpack[item].piece < 0:
                print("No",item,"left, attack is missed.")
                return 0
        elif className == "Melee":
            atkMod = obj.consumePotion("Battle")+int((obj.stats["STR"]-10)/2)
        
        if weapons[item].range < distance:
                print("\nTarget is out of range, attack is missed")
                return 0
        if className == "Ranged" and distance < 4:
                print("\nTarget is too close for a ranged weapon, attack is missed")
                return 0
        
        print(obj.name,"rolls for attack 'd20':",end=" ")
        attack = hitRoll("d20")[0]
        if obj.condition.get("Attack","") != "":
            if obj.condition["Attack"][0] >= 0:
                print("Accuracy is active.")
                attack = 30
        
        if obj.condition.get("Defense","") != "":
            print("Defense Breaker is active.")
            attack = 30

        if attack==1 or attack+atkMod < target.armor:
            print("MISS")
            return 0
        
        print("Damage Dice '"+str(obj.level)+weapons[item].dice+"':",end=" ")
        if className == "Ranged":
            obj.inventory.pouch[obj.inventory.backpack[item].ammo.name]-=1                
        elif className == "Throw":
            obj.inventory.backpack[item].change(-1,1)
        target.hurt(sum(hitRoll(str(obj.level)+weapons[item].dice))+atkMod,obj)

    
