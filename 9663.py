from sys import stdin
import copy


def solve(depth, y, x, listK):
    global count
    global inputN

    listN=copy.deepcopy(listK)
    if inputN == depth:
        count = count + 1
        print("hellow")
        return
    else:
        pass

    if y == inputN:
        return
    if depth == inputN-1 :
        for item in listN:
            print(item)
        print()
    for i in range(inputN):
        listN[y][i]=1
        listN[i][x]=1
    for i in range(inputN-y):
        if y+i < inputN  and x+i < inputN:
            listN[y+i][x+i] = 1
        if y+i < inputN  and x-i >= 0:
            listN[y+i][x-i] = 1
    for i in range(y+1):
        if y-i >= 0  and x-i >= 0:
            listN[y-i][x-i] = 1
        if y-i >= 0  and x+i < inputN:
            listN[y-i][x+i] = 1
    for i in range(y, inputN):
        for j in range(inputN):
            if listN[i][j]==0:
                # print(i,j)
                solve(depth+1, i, j, listN)


inputN = int(input())
count=0
y=0
x=0
listK = [[0 for _ in range(inputN)] for _ in range(inputN)]

print(0,0)
solve(0, y, x, listK)
print(count)
