from sys import stdin


def solve(depth):
    global M
    global N
    global visit
    global combination

    if depth == M:
        for item in combination:
            print(str(item) + " ", end= "")
        print()
        return

    for i in range(N):
        if visit[i] == False:
            visit[i] = True
            combination[depth]= i + 1
            solve(depth+1)
            visit[i]= False






N, M = map(int, stdin.readline().split())

visit = [False for _ in range(N)]
combination = [0 for _ in range(M)]

solve(0)
