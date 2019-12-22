from sys import stdin


testN = int(input())

for i in range(testN):
    a, b = map(int, stdin.readline().split())
    print("Case #%s: %s + %s = %s" %(i+1, a, b, a+b))
