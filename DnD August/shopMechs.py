from Dice import *
from Inventory import *

class ShopMech():
    def buy(obj,item,count=1):
        if not obj.isAlive: 
            print("Death character can not buy.") 
            return
        if item in armors:
            print("Armor trading not available for now.")
        if item in potions:
            item = potions[item]
            if obj.inventory.coin < item.price*count:
                count = int(obj.inventory.coin/item.price)
                print("You can not buy more than",count,item.name,"Potion")
            if item.name in obj.inventory.sack:
                obj.inventory.sack[item.name][1] += count
            else:
                obj.inventory.sack[item.name] = [item,count,0]
            obj.inventory.coin -= item.price*count
        else:
            item = weapons[item]
            if item.__class__.__name__ == "Throw":
                if obj.currentBackpack < item.size:
                    print("No slot in inventory for",item.name)
                    return
                if obj.inventory.coin < item.price*count:
                    count = int(obj.inventory.coin/item.price)
                    print("You can not buy more than",count,item.name)
                if obj.inventory.coin >= item.price*count:
                    obj.inventory.coin -= item.price*count
                    obj.inventory.backpack[item.name] = item
                    obj.currentBackpack-=item.size
                    obj.inventory.backpack[item.name].change(1,count)
                else:
                    print("Not enough money for",item.name)
                    return
            elif item.__class__.__name__ == "Ammo":
                if obj.currentPouch < count:
                    count = obj.currentPouch
                    if obj.inventory.coin < item.price*count:
                        count = int(obj.inventory.coin/item.price)
                    print("You can not buy more than",count,item.name)
                if obj.inventory.coin >= item.price*count:
                    obj.inventory.coin -= item.price*count
                    obj.inventory.pouch[item.name] += count
                    obj.currentPouch-=count
                else:
                    print("Not enough money for",item.name)
                    return
            else:
                if obj.currentBackpack < item.size:
                    print("No slot in inventory for",item.name)
                    return
                else:
                    if obj.inventory.coin >= item.price:
                        obj.inventory.coin -= item.price
                        obj.inventory.backpack[item.name] = item
                        obj.currentBackpack-=item.size
                    else:
                        print("Not enough money for",item.name)
                        return
        print("You buy",count,item.name,end="\n")

    def sell(obj,item,count=1):
        flag = False
        if not obj.isAlive: 
            print("Death character can not sell.")
            return
        if obj.inventory.backpack.get(item,"") != "":
            if weapons[item].__class__.__name__ == "Throw":
                if obj.inventory.backpack[item].piece < count:
                    count = obj.inventory.pouch[item].piece 
                    print("You can not sell more than",count,item)
            obj.inventory.coin += int(weapons[item].price/5)*count
            obj.inventory.backpack[item].change(-1,count)
            if  obj.inventory.backpack[item].piece == 0:
                obj.currentBackpack += weapons[item].size
                del obj.inventory.backpack[item]
            flag = True
        if obj.inventory.pouch.get(item,"") != "":
            if obj.inventory.pouch[item] < count:
                count = obj.inventory.pouch[item]
                print("You can not sell more than",count,item)
            obj.inventory.coin += int(ammos[item].price/5)*count
            obj.currentPouch += count
            obj.inventory.pouch[item] -= count
            flag = True
        if obj.inventory.sack.get(item,"") != "":
            if obj.inventory.sack[item][1] < count:
                count = obj.inventory.sack[item][1]
                print("You can not sell more than",count,item)
            obj.inventory.coin += int(potions[item].price/5)*count
            obj.inventory.sack[item][1] -= count
            flag = True

        if flag is True: print("You sell",count,item,end="\n")
        