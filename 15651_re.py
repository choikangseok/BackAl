from sys import stdin

def solve(depth):
    global N
    global M
    global visit
    global combination

    if depth == M :
        for item in combination:
            print(str(item)+ ' ', end="")
        print()
        return

    for i in range(N):
        # if (visit[i] == False):
            #i보다 작은 수들을 다 방문했다고 표기하기
                # visit[k]=True
        combination[depth]= i+1
        solve(depth+1)
            #i보다 작은 수들을 다 방문했다는 것을 취소!
            # for k in range(i+1):
            #     visit[k] = False





N, M = map(int, stdin.readline().split())


visit= [False for _ in range(N)]
combination = [0 for _ in range(M)]


solve(0)
