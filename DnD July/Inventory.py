from Weapons import *
from Potions import *
from Armor import *

class Inventory:
    def __init__(self,coin,armor = 0,backpack = {},pouch = {},sack = {},bag = {}):
        self.coin = coin
        self.armor = armor
        self.backpack = backpack
        self.pouch = pouch
        self.sack = sack
        self.bag = bag

    def show(self):
        print("\n\n--------------------------Inventory--------------------------\n")
        print("Inventory\tCoin:",self.coin,"\n")
        print(" Armor:")
        if self.armor != 0:
            self.armor.show()
        print("\n Backpack:")
        for item in self.backpack:
            self.backpack[item].show()
        print("\n Pouch:")
        for item in self.pouch:
            print("\t",self.pouch[item],item)
        print("\n Potion Sack:")
        for item in self.sack:
            print("\t",self.sack[item][1],item,"Potion")
        print("\n-------------------------------------------------------------\n")


kits = {
    "Barbarian":Inventory(800,armors["Leather"],{"Axe":weapons["Axe"]}),
    "Bard":Inventory(800,armors["Leather"],{"Short Sword":weapons["Short Sword"]}),
    "Cleric":Inventory(400,armors["Scale-Mail"],{"Short Bow":weapons["Short Bow"]},{"Arrow":9}),
    "Druid":Inventory(600,armors["Leather"],{"Sling":weapons["Sling"]},{"Pebble":12}),
    "Fighter":Inventory(800,armors["Scale-Mail"],{"Falx":weapons["Falx"]}),
    "Monk":Inventory(400,0,{"Knuckleduster":weapons["Knuckleduster"]}),
    "Paladin":Inventory(2400,armors["Scale-Mail"],{"Longsword":weapons["Longsword"]}),
    "Ranger":Inventory(800,armors["Leather"],{"Crossbow":weapons["Crossbow"]},{"Arrow":15}),
    "Rouge":Inventory(1600,armors["Leather"],{"Boomerang":weapons["Boomerang"]}),
    "Sorcerer":Inventory(1200,0,{"Dagger":weapons["Dagger"]}),
    "Wizard":Inventory(1800,0,{"Quarterstaff":weapons["Quarterstaff"]}),

}
