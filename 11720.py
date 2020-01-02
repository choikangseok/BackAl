from sys import stdin


testN = int(stdin.readline())

test = str(stdin.readline().replace("\n",""))

total=0
for item in test:
    total = total + int(item)

print(total)
