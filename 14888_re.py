from sys import stdin


def cal(combination):
    global listA
    global result_all
    result = listA[0]
    for i in range(len(combination)):
        if combination[i] == '+':
            result = result + listA[i+1]
        if combination[i] == '-':
            result = result - listA[i+1]
        if combination[i] == '*':
            result = result * listA[i+1]
        if combination[i] == '/':
            if result < 0 :
                result = -((-result) // listA[i+1])
            else:
                result = result // listA[i+1]


    result_all.append(result)

def solve(depth):
    global N
    global listA
    global combination
    global list_Cal
    global cal_str


    if depth == N-1 :
        # print(combination)
        cal(combination)
        return
        #계산 한걸 출력하기

    for i in range(N-1):
        # print('i', i)
        if visit[i]== False:
            combination[depth]= cal_str[i]
            visit[i]=True
            solve(depth+1)
            visit[i]=False



N = int(input())
listA = list(map(int, stdin.readline().split()))
list_Cal = list(map(int, stdin.readline().split()))
# print(list_Cal)
combination= ['' for _ in range(N-1)]
cal_str = str('+'*list_Cal[0] + '-'*list_Cal[1] + '*'*list_Cal[2] + '/'*list_Cal[3])
# print(cal_str)
visit = [False for _ in range(len(cal_str))]
result_all=[]

solve(0)
# print(result_all)

print(max(result_all))
print(min(result_all))

#cal의 순서는 +, -, x, /
