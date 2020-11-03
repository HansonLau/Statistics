import random


def check(combo, space):
    count = 0
    for i in range(len(space)):
        if combo == space[i]:
            count += 1
    if count >= 2:
        return False
    return True

# heads and tails only for now
def f(quantity):
    sampleSpaceSize = 2**quantity # might not be needed
    sampleSpace = [[]]*sampleSpaceSize # ^^ will be needed for this
    names = ["H","T"] 


    for i in range(sampleSpaceSize):
        counter = 0
        while True:
            for j in range(2):
                x = random.randint(0,1)
                sampleSpace[i].append(names[x])
            print(sampleSpace[i])
            if counter > 20:
                break
            if not(check(sampleSpace[i], sampleSpace)):
                sampleSpace[i].clear()
                counter +=1
                continue
            else:
                break
                
    print("done")
    print(sampleSpace)
'''
0000
1000
0100
0010
0001
1100
0110
0011
1001
1010
0101
1110
0111
1101
1011
1111
'''
'''
000
100
010
001
110
011
101
111
'''
'''
00
01
10
11
'''
    
while True:
    typ = input("Flipping coins (f) or stop (s) ")

    if typ == "f" or typ =="F":
        quantity = int(input("How many coins? "))
        f(quantity)
    elif typ == "s" or typ =="D":
        break
    else:
        continue