class Potion():
    def __init__(self,name,price,attribute,duration):
        self.name = name
        self.price = price
        self.attribute = attribute
        self.duration = duration

potions = {
    "Charm":Potion("Charm",100,(2,"CHA"),2),
    "Battle":Potion("Battle",100,(2,"STR"),2),
    "LesserHealth":Potion("Lesser Health",25,(),0),
    "Health":Potion("Health",50,(),0),
    "GreaterHealth":Potion("Greater Health",100,(),0),
    "SuperHealth":Potion("Super Health",200,(),0),
    "Invisibility":Potion("Invisibility",400,(0,0),3),
    "Resistance":Potion("Resistance",100,(),2),
    "Sense":Potion("Sense",200,(2,"WIS"),2),
    "Speed":Potion("Speed",150,(2,"DEX"),2),
    "Dick":Potion("Dick",100,(20,"CHA"),20)
}
