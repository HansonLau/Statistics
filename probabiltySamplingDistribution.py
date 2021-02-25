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

def round(num):

    #round to hundreths place

    # Ex : .3154
    num += .005
    # .3204
    num *= 100
    # 32.04
    num //= 1
    # 32
    return num/100
    # .32

def simulate(l, s):
    total = []
    for i in range(s):
        x = random.randint(0,99)
        total.append(l[x])
    
    return round(sum(total)/s)

def getDistinct(nums):
        #insert list to set
    list_set = set(nums)
        # convert the set to the list
    return (list(list_set))

def getOccurances(nums):
    unique = getDistinct(nums)
    occurances = [0]*(len(unique))
    temp = nums
    for i in range(len(unique)):
        for j in range(len(temp)):
            if unique[i] == temp[j]:
                occurances[i] += 1
    return occurances

def graph(x, frequencies):
    plt.plot(x, frequencies, 'ro')
    plt.axis([min(x)-.1, max(x)+.1, 0, max(frequencies)+5]) # [xmin, xmax, ymin, ymax]
    plt.show()

newList = generateList(proportion, bigList)

data = []

for i in range(simulations):
    data.append(simulate(newList, sampleSize))

# tests
#print(data)
#print(getOccurances(data))

# makes dotplot graph, every dot represents and occurance per proportion
graph(getDistinct(data), getOccurances(data))
