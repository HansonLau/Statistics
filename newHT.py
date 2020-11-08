
times = int(input("How many coins? "))

sampleSpace = []
for i in range(2**times):
    sampleSpace.append("")

names = ["H", "T"]

for i in range(2**times):
    sampleSpace[i] = names[i%2]
    # print(sampleSpace[i])
    for j in range(times-1):
        sampleSpace[i] += names[(j+(i%2))%2]

    # for j in range(times):
        # sampleSpace[i] += names[(j+i)%2]


print(sampleSpace)

'''
h
t

hh
ht
th
tt

hhh
hht
hth
htt
thh
tht
tth
ttt

hhhh
hhht
hhth
hhtt
hthh
htht
htth
httt
thhh
thht
thth
thtt
tthh
ttht
ttth
tttt
'''