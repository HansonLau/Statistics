
times = int(input("How many coins? "))
sampleSpace = []

for i in range(2**times):
    sampleSpace.append([])

names = ["H", "T"]

for i in range(len(sampleSpace)):

    sampleSpace[i].append(names[i])

print(sampleSpace)

'''
h
t

hh
tt
ht
th

hhh
htt
hht
hth
thh
ttt
tht
tth

hhhh
hhtt
hhht
hhth
hthh
httt
htht
htth
thhh
thtt
thht
thth
tthh
tttt
ttht
ttth
'''