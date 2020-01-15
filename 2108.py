from sys import stdin
from collections import Counter
import math
inputN = int(stdin.readline())
listN = list()
total=0
dicK = {}

for _ in range(inputN):

    inta = int(stdin.readline())
    listN.append(inta)

listMost = Counter(listN)
listMost = sorted(listMost.items(),key= lambda x: x[1], reverse=True)
listonlyM= list()

for item in listMost:
    if item[1]==listMost[0][1]:
        listonlyM.append(item[0])
listonlyM.sort(reverse = True)

for item in range(len(listN)):
    total = total + listN[item]

print('%.0f' % (total/inputN))
listN.sort()
print(listN[inputN//2])
if len(listonlyM) == 1 :
    print(listMost[0][0])
else:
    print(listonlyM[-2])
print(listN[-1] - listN[0])
