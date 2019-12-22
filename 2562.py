from sys import stdin

listN = list()
count = 1;

for _ in range(9):
    listN.append(int(stdin.readline()))

big = listN[0]
for i in range(8):
    if listN[i+1] > big:
        big = listN[i+1]
        count = i+1

print(big)
print(count)
