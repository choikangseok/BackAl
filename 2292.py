from sys import stdin


inputNum = int(input())


i=0
k=1
while True:
    k = k + 6 *i
    if inputNum <= k:
        break
    i= i+1
print(i+1)
