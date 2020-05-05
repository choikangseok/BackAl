from sys import stdin


def solve(num, N):
    NN=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    queue= []

    # t*m 만 정도는 해야한다.
    for i in range(num+1):
        A=''
        while True:
            # print(i%N)
            A= NN[i%N]+A
            # queue.append(NN[i%N])
            i = i//N
            if i ==0:
                break
        for item in A :
            queue.append(item)
    return queue



#숫자를 진법에 맞게 큐를 해야함
N = int(input())
T = int(input())
M = int(input())
P = int(input())
# result=[]
# print(solve(12, 2))
Numlist= solve(T*M, N)
print(Numlist)

# print(solve(t*m, N))
#n진
#t개 만큼 프린트하면되는 것
#P는 튜브의 순서
#M 게임에 참가하는 인원
i=0
#for문 start stop step
result=''
for i in range(T):
    result = result + Numlist[i*M+P-1]

print(result)
# for i in range(P, T*M, M):
#     print(Numlist[i])
# num
# count=0

#T의 개수 만큼 출력
