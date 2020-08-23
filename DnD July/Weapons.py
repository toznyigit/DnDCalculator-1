class Ammo:
    def __init__(self,name,price,kind):
        self.name = name
        self.kind = kind
        self.price = price

class Weapons:
    def __init__(self,name,price,damage,size,flag,_range,kind):
        self.name = name
        self.price = price
        self.isMartial = flag
        self.dice = damage
        self.size = size
        self.range = _range
        self.kind = kind

class Ranged(Weapons):
    def __init__(self,name,price,damage,size,flag,kind,_range,ammotype):
        super().__init__(name,price,damage,size,flag,_range,kind)
        self.ammo = ammotype
    def show(self):
        print("\t",self.name,"["+self.__class__.__name__,":",self.kind+"]")
        print("\t\tDamage:",self.dice,"\tRange:",self.range,"\tAmmo:",self.ammo.name)

class Melee(Weapons):
    def __init__(self,name,price,damage,size,flag,kind,_range):
        super().__init__(name,price,damage,size,flag,_range,kind)
    def show(self):
        print("\t",self.name,"["+self.__class__.__name__,":",self.kind+"]")
        print("\t\tDamage:",self.dice,"\tRange:",self.range)

class Throw(Weapons):
    def __init__(self,name,price,damage,size,flag,kind,_range,influence):
        super().__init__(name,price,damage,size,flag,_range,kind)
        self.piece = 0
        self.influence = influence
    def change(self,mod,piece):
        self.piece+=piece*mod
    def show(self):
        print("\t",self.name,"["+self.__class__.__name__,":",self.kind+"]")
        print("\t\tDamage:",self.dice,"\tRange:",self.range)
        print("\t\t"+self.influence,"Effect\tPiece:",self.piece)
    
ammos = {
    "Arrow":Ammo("Arrow",25,"Bow"),
    "Pebble":Ammo("Pebble",5,"Sling"),
}
weapons = {
    "Short Bow":Ranged("Short Bow",2500,"d6",1,False,"Bow",5,ammos["Arrow"]),
    "Long Bow":Ranged("Long Bow",7500,"2d8",3,True,"Bow",10,ammos["Arrow"]),
    "Crossbow":Ranged("Crossbow",5000,"d10",2,False,"Bow",8,ammos["Arrow"]),
    "Boomerang":Ranged("Boomerang",6000,"d8",2,True,"Boomerang",4,0),
    "Sling":Ranged("Sling",1000,"d4",1,True,"Sling",5,ammos["Pebble"]),
    "Dagger":Melee("Dagger",1000,"d4",1,False,"Dagger",0),
    "Knuckleduster":Melee("Knuckleduster",10000,"d20",1,True,"Knuckleduster",0),
    "Quarterstaff":Melee("Quarterstaff",1000,"2d4",1,False,"Staff",1),
    "Short Sword":Melee("Short Sword",1200,"d6",1,False,"Sword",1),
    "Falx":Melee("Falx",1200,"2d6",1,False,"Sword",1),
    "Longsword":Melee("Longsword",2000,"d10",2,False,"Sword",2),
    "Axe":Melee("Axe",2000,"d10",1,False,"Axe",1),
    "Mace":Melee("Mace",2500,"d12",1,True,"Mace",1),
    "Spear":Melee("Spear",500,"d6",2,False,"Spear",3),
    "Warhammer":Melee("Warhammer",7500,"2d10",3,True,"Hammer",1),
    "Greatsword":Melee("Greatsword",5000,"2d12",3,True,"Sword",2),
    "Arrow":Ammo("Arrow",25,"Bow"),
    "Pebble":Ammo("Pebble",5,"Sling"),
    "Bomb":Throw("Bomb",500,"d8",2,True,"Bomb",3,"Area"),
    "Knife":Throw("Knife",50,"d4",1,False,"Knife",3,"Spot"),
    "Javelin":Throw("Javelin",100,"d6",3,False,"Javelin",4,"Spot")
}