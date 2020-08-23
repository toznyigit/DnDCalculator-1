import time,sys

classDir = {
    "Bard":[0,{}],
    "Cleric":[0,{}],
    "Druid":[0,{}],
    "Paladin":[0,{}],
    "Ranger":[0,{}],
    "Sorcerer":[0,{}],
    "Warlock":[0,{}],
    "Wizard":[0,{}],
}

f = open("Magics","r")

for line in f:
    unique = True
    classes = []
    line = line[:-1]
    lvl = ""
    for item in (line.split(": ")[1]).split(","):
        if item.__contains__("\t"):
            lvl = item[-5]
            break
        if not item.__contains__("#"): classes.append(item)

    spell = line.split(": ")[0]
    i = 1
    for _class in classes:
        if i>1: unique = False
        i+=1
    for _class in classes:
        if classDir[_class][1].get(lvl,"") == "": classDir[_class][1][lvl] = [0,[]]
        if unique: spell+=" [U]"
        classDir[_class][1][lvl][1].append(spell)
        classDir[_class][1][lvl][0]+=1
        classDir[_class][0]+=1

f.close()

for item in classDir:
    name = item
    item = classDir[item]
    print("\n","-"*100)
    print("\t"*4,name,"number of spell:",item[0])
    time.sleep(0.5)
    for lvl in range(6):
        if item[1].get(str(lvl),"") == "":
            print("\n",0,"Level",lvl,"spells:")
            continue
        print("\n",item[1][str(lvl)][0],"Level",lvl,"spells:")
        i=0
        for spells in item[1][str(lvl)][1]:
            if i%8 == 0: print("\n")
            sys.stdout.write("%s \t"%(spells))
            sys.stdout.flush()
            time.sleep(0.1)
            i+=1
        print("\n")
    print("\n","-"*95)
    time.sleep(0.1)

print("\n")