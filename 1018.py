from sys import stdin

a, b = map(int, stdin.readline().split())

listN = list()
for i in range(a):
    strN = list(stdin.readline().replace("\n", ""))
    listN.append(strN)
listA = list()

for i in range(8):
    strN = list()
    for k in range(8):
        if (( k % 2) + (i % 2)) % 2 == 0 :
            strN.append('W')
        else :
            strN.append('B')
    listA.append(strN)

listB = list()

for i in range(8):
    strN = list()
    for k in range(8):
        if (( k % 2) + (i % 2)) % 2 == 0 :
            strN.append('B')
        else :
            strN.append('W')
    listB.append(strN)

countA = 0
countB = 0
min = 64



for j in range(a-7):
    for w in range(b-7):
        countA = 0
        countB = 0
        for i in range(8):
            for k in range(8):
                if listN[j+i][w+k] != listA[i][k]:
                    countA = countA + 1
                if listN[j+i][w+k] != listB[i][k]:
                    countB = countB + 1
        if countA > countB:
            if min > countB:
                min=countB
        else :
            if min > countA:
                min=countA

print(min)
