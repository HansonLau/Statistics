import random
import time
import matplotlib as plt
 
# This program tests to see if something
# is statistcally siginificant or not
# With 100 tests
 
 
loops = 100
 
numberOfOutcomes = int(input("How many outcomes? "))
population = int(input("What is the sample size? "))
 
# Initializes list with zeroes
data1 = [0]*numberOfOutcomes  # answer from people
data2 = [[]]*numberOfOutcomes  # proportion/ how many times it occured
 
 
# Assign randomness
for i in range(loops):
    for j in range(population):
        r = random.randint(0,numberOfOutcomes-1)
        data1[r] += 1
    for k in range(numberOfOutcomes):
        data2[k].append(data1[k]/population) # proportion
    data1 = [0]*numberOfOutcomes
 
index = 0
for i in range(len(data2)):
    if (max(data2[i]) - min(data2[i])) > (max(data2[index]) - min(data2[index])):
        index = i
 
 
finalList = []
for i in range(len(data2)):
    finalList += data2[i]
 
uniqueNumbers = set(finalList) # Finds unique numbers in the combined list
categories = []   # Set labels for x axis
for number in uniqueNumbers:
    categories.append(number)
print(categories)
time.sleep(10)
 
data3 = []*len(uniqueNumbers)  # occurences per unique proportion
 
for i in range(uniqueNumbers):
    data3[i] = counter(categories[i], finalList)  # assigns number of occurences
 

def counter(proportion, list):  # Counts occurences
    counter = 0
    for i in range(len(list)):
        if proportion == list[i]:
            counter += 1
    return counter


