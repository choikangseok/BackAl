from sys import stdin

def solve(depth):
    global N
    global visit
    global combination

    if depth == M :
        for item in combination:
            print(str(item),end=" ")
        print()
        return
    for i in range(N):
        if not visit[i] :
            combination[depth] = i+1
            for k in range(i+1):
                visit[k]=True
            solve(depth + 1)
            for k in range(i+1):
                visit[k]=False



N, M = map(int, stdin.readline().split())

visit = [False for _ in range(N)]
combination = [0 for _ in range(M)]
solve(0)
