from sys import stdin
import copy




listN= [1,2,3,4,5,6]
listNK= [1,2,3]

listN=list(set(listN) - set(listNK))

print(listN)

if listN == []:
    print("시발")
