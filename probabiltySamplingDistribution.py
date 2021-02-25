import matplotlib.pyplot as plt
import random


proportion = float(input("Enter proportion ex: .13 (INCLUDE DECIMAL): "))
sampleSize = int(input("Enter sample size ex: 200 : "))
simulations = int(input("Enter numner of simulations ex: 100 : "))

bigList = [0]*100

def generateList(p, l):
    temp = int(p*100)
    for i in range(temp):
        l[i] = 1
    return l

def simulate(l, s):
    total = []
    for i in range(s):
        x = random.randint(0,99)
        total.append(l[x])
    
    return sum(total)/s

newList = generateList(proportion, bigList)

data = []

for i in range(simulations):
    data.append(simulate(newList, sampleSize))

print(data)