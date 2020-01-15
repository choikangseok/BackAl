from sys import stdin

numN = int(stdin.readline())
listN = list()
for _ in range(numN*2):
    listN.append(int(stdin.readline()))

i=0
for _ in range(numN):
    count=0
    k=listN[i]
    n=listN[i+1]

    if k == 0 :
        break
    else:
        listNN = [[0]*n for row in range(k+1)]

    for j in range(k+1):
        for l in range(n):
            if j == 0 :
                count = count +1
                listNN[j][l] = count
            else:
                listNN[j][l] = listNN[j-1][l] + listNN[j][l-1]
    print(listNN[k][n-1])
    # print(listNN[k-1][n-1])
    i= i+2
