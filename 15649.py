from sys import stdin


a, b = map(int, stdin.readline().split())

listN= list()
for _ in range(b):
    listN.append(1)


while True:
    for i in range(len(listN)):
        if listN[-i-1] > a and (-i-2 > -(b+1)) :
            listN[-i-2]= listN[-i-2] +1
            if listN[0] != a+1:
                listN[-(i+1)] =1
    if listN[0] > a:
        break
    if len(set(listN))==b:
        for item in listN:
            print(str(item) + " ",end="")
        print()
    listN[b-1]= listN[b-1] +1
