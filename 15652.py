from sys import stdin

def solve(depth):
    global M
    global N
    global combination

    if depth == M:
        for item in combination:
            print(str(item) + " ", end="")
        print()
        return

    for i in range(N):
        combination[depth]= i+1
        if depth >=1:
            if combination[depth] >= combination[depth-1]:
                solve(depth+1)
        else:
            solve(depth+1)


N, M = map(int, stdin.readline().split())

# visit = [False for _ in range(N)]
combination = [0 for _ in range(M)]

solve(0)
