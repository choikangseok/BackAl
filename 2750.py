from sys import stdin

inputN = int(input())
listN= list()
for _ in range(inputN):
    listN.append(int(input()))

listN.sort()
for item in listN:
    print(item)
