# from sys import stdin
# import copy
#
# def solve(listZ, listN):
#
#     if listZ == []:
#         for i in range(9):
#             for j in range(9):
#                 print(str(listN[i][j]) + " ", end='')
#             print()
#         sys.exit(0)
#     y = listZ[0][0]
#     x = listZ[0][1]
#
#     listZero = copy.deepcopy(listZ)
#     newlistN= copy.deepcopy(listN)
#     setN = {1,2,3,4,5,6,7,8,9}
#     for i in range(9):
#         setN = setN - {newlistN[y][i]} - {newlistN[i][x]}
#     for i in range((y//3)*3 , (y//3)*3 +3):
#         for j in range((x//3)*3 , (x//3)*3 +3):
#             setN = setN - {newlistN[i][j]}
#     listZero.pop(0)
#     for item in setN:
#         newlistN[y][x] = item
#         #print("solve : ", listZero)
#         solve(listZero, newlistN)
#     return
#
# listN = []
# listZero = []
# for _ in range(9):
#     listN.append(list(map(int, stdin.readline().replace('\n', '').split(" "))))
#
# for i in range(9):
#     for j in range(9):
#         if listN[i][j] == 0:
#             listZero.append((i,j))
# #print(listZero)
# solve(listZero, listN)

from sys import stdin
import sys
def solve(depth):
    if depth == len(listZero):
        for i in range(9):
            for j in range(9):
                print(str(listN[i][j]) + " ", end='')
            print()
        sys.exit(0)
    y=listZero[depth][0]
    x=listZero[depth][1]

    for k in range(1,10):
        flag=True
        for i in range(9):
             if k == listN[y][i] or k == listN[i][x]:
                 flag=False
                 break
        if flag == False:
            continue
        for i in range((y//3)*3 , (y//3)*3 +3):
            for j in range((x//3)*3 , (x//3)*3 +3):
                if listN[i][j] == k:
                    flag=False
                    break
            if flag == False:
                break
        if flag == False :
            continue
        listN[y][x] = k
        solve(depth+1)
        listN[y][x] = 0

listN = []
listZero = []
for _ in range(9):
    listN.append(list(map(int, stdin.readline().replace('\n', '').split(" "))))

for i in range(9):
    for j in range(9):
        if listN[i][j] == 0:
            listZero.append((i,j))
solve(0)
