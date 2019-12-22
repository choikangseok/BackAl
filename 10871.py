from sys import stdin


testN, testX = map(int, stdin.readline().split())

listN = list(map(int, stdin.readline().split()))
result =''

for i in listN:
    if i < testX:
        result = result + str(i) + ' '
print(result)
