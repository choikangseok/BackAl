from sys import stdin


testN = int(input())

for i in range(testN):
    a, b = map(int, stdin.readline().split())
    print("Case #%s: %s" %(i+1, a+b)
