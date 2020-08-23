import random
import time

value = 0

dices = ("d4","d6","d8","d10","d12","d20")

def roll(dice):
    diceList = []
    times = dice.split('d')[0]
    if times == "": times = 1
    faces = dice.split('d')[1]
 
    for i in range(int(times)):
        _dice = random.randint(1, int(faces))
        diceList.append(_dice)
    return diceList

def hitRoll(dice):
    diceList = []
    times = dice.split('d')[0]
    if times == "": times = 1
    faces = dice.split('d')[1]
 
    for i in range(int(times)):
        _dice = random.randint(1, int(faces))
        diceList.append(_dice)
        print(_dice,end =", ")
        time.sleep(value)
    return diceList

def playerRoll(dice):
    diceList = []
    times = dice.split('d')[0]
    if times == "": times = 1
    faces = dice.split('d')[1]
    if 'd'+faces in dices:
        for i in range(int(times)):
            _dice = random.randint(1, int(faces))
            diceList.append(_dice)
            print(_dice),
            time.sleep(0.4)
        return diceList
    else:
        print("Available dices: "),
        for item in dices:
            print(item),
        print("")
        roll(input("Choose valid dice: "))



