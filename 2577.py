from sys import stdin


A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

listN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = list(str(A * B * C))


for item in result:
    listN[int(item)]= listN[int(item)] + 1

for N in listN:
    print(N)
