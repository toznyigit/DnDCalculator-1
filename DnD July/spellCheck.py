from Player import Player
from Enemy import *
from Spell import *
import time

spell = DeathH()
spell2 = DeathW()
Dick = Player("Dick","Barbarian","Human",("Athletics","Stealth"))
newEnemy = Enemy(randomSpecies(Dick.level+8))
spell2.use(Dick)

while True:
    if not newEnemy.isAlive or not Dick.isAlive:
        break
    print("")
    Dick.attack("Axe",newEnemy,1)
    time.sleep(0.3)
    newEnemy.showHP()
    time.sleep(1)
    if not newEnemy.isAlive or not Dick.isAlive:
        break
    print("")
    newEnemy.attack(Dick)
    newEnemy.showHP()
    time.sleep(0.3)
    Dick.showHP()
    time.sleep(1)