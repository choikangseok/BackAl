from sys import stdin


strN = str(stdin.readline().replace("\n",""))

listN =['ABC', 'DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']
total=0
for item in strN:
    for i in range(len(listN)):
        if item in listN[i]:
            total= total + 3 + i
print(total)
