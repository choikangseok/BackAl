from sys import stdin


TestN  = int(input())


for _ in range(TestN):
    a, b = map(int, stdin.readline().split())
    print(a+b)
