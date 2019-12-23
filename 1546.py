from sys import stdin


subjectN = float(stdin.readline())

listN = list(map(float, stdin.readline().split()))

listN.sort()

Max=listN[-1]

listTotal = 0.0
for item in listN:
    listTotal= listTotal + item
average = listTotal / Max * 100 / len(listN)
print(average)
