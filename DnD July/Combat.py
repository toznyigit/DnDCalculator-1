from Player import *
from Enemy import *

print("Player is calculating")
time.sleep(1)
Dick = Player("Dick","Barbarian","Human",("Athletics","Stealth"))
Dick.gainExp(63999)
Dick.show()


print("Enemy is calculating")
time.sleep(1)
newEnemy = Enemy(randomSpecies(Dick.level+2))
newEnemy.show()
time.sleep(0.5)

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
    time.sleep(0.3)
    Dick.showHP()
    time.sleep(1)


