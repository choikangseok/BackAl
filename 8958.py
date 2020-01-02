from sys import stdin



testN = int(stdin.readline())
listN =[]
for i in range(testN):
    listN.append(stdin.readline().replace("\n",""))

#주석입니다.
#파이썬은 readline을 할때 개행까지 같이가져옵니다.

for item in listN:
    score=0
    total=0
    for Ditem in item:
        if Ditem =='O':
            score = score + 1
        else:
            score = 0
        total = total + score
    print(total)
