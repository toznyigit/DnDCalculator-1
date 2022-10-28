import random

def add(x,y):
  return x+y

def mod(x,y):
  return x**y

print(add(5,6))

def multiPorpuseDice(faces):
  result = 0
  theArray = []
  for i in range(1,faces+1):
      theInt = random.randint(i,10000)
     result+= theInt
      theArray.append(theInt)
      
  print(sum(theArray))
  return result//faces

if __name__ == '__main__':
  print(multiPorpuseDice(add(mod(8,16),mod(17,24))))
