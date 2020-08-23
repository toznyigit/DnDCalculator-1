class Armor:
    base = (2,11,14,16)
    upgradeCost = (500,1200,2500,6000,11000)
    def __init__(self,name,price,weight,advantage):
        self.name = name
        self.price = price
        self.level = 0
        self.advantage = advantage
        self.weight = weight

    def upgrade(self):
        self.level+=1
    def show(self):
        print("\t",self.name,"Armor","\tLevel:",self.level)
        print("\t\tPerks:",end=" ")
        for perk in self.advantage:
            print(perk,end=", ")
        print("")
    
    @property
    def protect(self):
        return Armor.base[self.weight]+self.level
    def cost(self):
        return Armor.upgradeCost[self.level]
        
armors = {
    "Leather":Armor("Leather",500,1,()),
    "Scale-Mail":Armor("Scale-Mail",5000,2,("-Stealth")),
    "Chain-Mail":Armor("Chain-Mail",7500,3,("-Stealth")),
    "Shield":Armor("Shield",1000,0,())
}