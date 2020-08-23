import os
magiclist = []

sort = open("Magics","r")

for line in sort:
    magiclist.append(line)
sort.close()

magiclist.sort()

paste = open("Sihir","a+")

for item in magiclist:
    paste.write(item)

paste.close()
os.system("mv Sihir Magics")