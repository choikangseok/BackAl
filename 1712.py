from sys import stdin

A, B, C = map(int, stdin.readline().split())


N=1


D = C-B

if D <= 0:
    print("-1")
else:
    print(A//D+1)
