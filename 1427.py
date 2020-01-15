from sys import stdin

inputnum = str(input())
listN = list()
for i in inputnum:
    listN.append(int(i))

listN.sort(reverse=True)

for i in listN:
    print(i, end='')
