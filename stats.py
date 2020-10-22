import random
import time
import matplotlib.pyplot as plt
 
# This program tests to see if something
# is statistcally siginificant or not
# With 100 tests
# This program only works with 2 outcomes for now

def counter(proportion, list):  # Counts occurences
    counter = 0
    for i in range(len(list)):
        if proportion == list[i]:
            counter += 1
    return counter

def graph(x, frequencies):
    plt.plot(x, frequencies, 'ro')
    plt.axis([min(x)-.1, max(x)+.1, 0, max(frequencies)+5]) # [xmin, xmax, ymin, ymax]
    plt.show()
 
def round(num): # rounds to hundreths place
    num *= 1000
    num = int(num)
    num += 5
    num //= 10
    return float(num/100)
 
numberOfOutcomes = int(input("How many outcomes? "))
loops = 1
population = int(input("What is the sample size? "))
 
# Initializes list with zeroes
data1 = [0]*numberOfOutcomes  # answer from people
data2 = [0]*loops # proportion/ how many times it occured
 
# Assign randomness
for i in range(loops):
    for j in range(population):
        r = random.randint(0,numberOfOutcomes-1) # fix this
        data1[r] += 1

    data2[i] = round((data1[0]/population)) # proportion
    data1 = [0]*numberOfOutcomes
'''
finalList = []
for i in range(len(data2)):
    finalList += data2[i]
'''
uniqueNumbers = set(data2) #set(finalList) # Finds unique numbers in the combined list
categories = []   # Set labels for x axis
for number in uniqueNumbers:
    categories.append(number)
#print(categories)
 
data3 = [0]*len(uniqueNumbers)  # occurences per unique proportion
 
for i in range(len(uniqueNumbers)):
    data3[i] = counter(categories[i], data2) #finalList)  # assigns number of occurences
 
graph(categories, data3)



