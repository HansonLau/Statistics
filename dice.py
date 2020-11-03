# This program shows sample space for dice

def display(sampleSpace, sides):

    for i in range(len(sampleSpace)):
        print(sampleSpace[i], end="")
        if (i+1)%sides == 0:
            print("")

# two dices only for now
def d(sides, dices):
    sampleSpaceSize = sides**dices # might not be needed
    sampleSpace = [[]]*sampleSpaceSize

    used = 0
    for i in range(sides):

        for j in range(sides):

            sampleSpace[i+j+used] = [i+1, j+1]
        used += sides-1
    display(sampleSpace, sides)

while True:
    typ = input("Rolling dice (d) or stop (s) ")

    if typ == "d" or typ =="D":
        sides = int(input("Enter number of sides "))
        dices = int(input("How many dices? "))
        d(sides, dices)
    elif typ == "s" or typ =="D":
        break
    else:
        continue

