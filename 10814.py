from sys import stdin


inputN = int(input())
listN= list()
for _ in range(inputN):
    a, b = stdin.readline().split()
    listN.append((int(a), b))
listN.sort(key=lambda x : x[0])

for item in listN:
    print("%s %s" % (item[0], item[1]))
