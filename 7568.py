from sys import stdin
import copy


inputN = int(input())
listN = list()

for _ in range(inputN):
    a, b = map(int, stdin.readline().split())
    listN.append([a,b, 0])
listNinit = copy.deepcopy(listN)
listN3 = copy.deepcopy(listN)
listN.sort(reverse = True, key = lambda x: x[0])
listN1 = copy.deepcopy(listN)
listN.sort(reverse = True, key = lambda x: x[1])
listN2 = copy.deepcopy(listN)


rank = 1
for i in range(len(listN1)):
    if (i > 0) and listN1[i-1][0] == listN1[i][0]:
         listN1[i][2] = copy.deepcopy(listN1[i-1][2])
    else:
         listN1[i][2] = rank

    rank = rank +1
rank = 1
for i in range(len(listN2)):
    if (i > 0) and listN2[i-1][0] == listN2[i][0]:
         listN2[i][2] = copy.deepcopy(listN2[i-1][2])
    else:
         listN2[i][2] = rank
    rank = rank +1



for i in range(len(listNinit)):
    for j in range(len(listN1)):
        if (listNinit[i][0] == listN1[j][0]) and (listNinit[i][1] == listN1[j][1]):
            listNinit[i][2] = copy.deepcopy(listN1[j][2])


for i in range(len(listNinit)):
    for j in range(len(listN2)):
        if (listNinit[i][0] == listN2[j][0]) and (listNinit[i][1] == listN2[j][1]):
            if listN2[j][2] < listNinit[i][2] :
                listN3[i][2] = copy.deepcopy(listNinit[i][2])
            else:
                listN3[i][2] = copy.deepcopy(listN2[j][2])


for i in range(len(listNinit)):
    for j in range(len(listN2a)):
        if (listNinit[i][0] == listN2[j][0]) and (listNinit[i][1] == listN2[j][1]):
            if listNinit[i][2] > listN2[j][2]:
                listNinit[i][2] = copy.deepcopy(listN2[j][2])
print (listNinit)
print (listN1)
print (listN2)
print (listN3)
for i in range(len(listNinit)):
    count=1
    for j in range(len(listN3)):
        if listN3[j][2] < listNinit[i][2] :
            count = count +1
    if listNinit[i][2] > count:
        listNinit[i][2]=count

strResult = ""
for i in range(len(listNinit)):
    strResult = strResult + str(listNinit[i][2]) +" "
print(strResult)
