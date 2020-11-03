
def display(sampleSpace, quantity):
    for i in range(len(sampleSpace)):
        print(sampleSpace[i], end="")
        if i+1 % quantity == 0:
            print(" ")

# heads and tails only for now
def f(quantity):
    sampleSpaceSize = 2**quantity # might not be needed
    sampleSpace = [[]]*sampleSpaceSize # ^^ will be needed for this
    names = ["H","T"] 
    loop = sampleSpaceSize//2

    for i in range(quantity):
        for j in range(loop):
            if j%2 == 0:
                sampleSpace[i].append(names[0])
            else:
                sampleSpace[i].append(names[1])
        loop //= 2
    display(sampleSpace, quantity)

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