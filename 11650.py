from sys import stdin

inputN = int(input())
listN= list()
for _ in range(inputN):
    a, b = map(int, stdin.readline().split())
    listN.append((a, b))

listN.sort(key = lambda x :( x[0], x[1]))


for i in range(inputN):
    print(str(listN[i][0]) + " " + str(listN[i][1]))
