from sys import stdin
import copy






inputN = int(input())
count = 0
y=3
x=4
listN = [[0 for _ in range(inputN)] for _ in range(inputN)]

for i in range(inputN):
    listN[y][i]=1
    listN[i][x]=1
for i in range(inputN-y):
    if y+i < inputN  and x+i < inputN:
        listN[y+i][x+i] = 1
    if y+i < inputN  and x-i >=0:
        listN[y+i][x-i] = 1
for i in range(y+1):
    if y-i >= 0  and x-i >= 0:
        listN[y-i][x-i] = 1
    if y-i >= 0  and x+i < inputN:
        listN[y-i][x+i] = 1


for item in listN:
    print(item)
