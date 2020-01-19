from sys import stdin
import copy




def solve(depth, listN):
    global count
    global inputN
    if depth == inputN:
        count = count + 1
        return

    for i in range(inputN):
        newlistN = copy.deepcopy(listN)

        if newlistN[depth][i] != 1:
            for k in range(inputN):
                #세로줄 가로줄 다 1로 초기화
                newlistN[depth][k] = 1
                newlistN[k][i] = 1
            j=1
            while True:
                flag= False
                if (depth+j < inputN) and (i+j < inputN):
                    newlistN[depth +j][i+j]=1
                    flag = True
                    #1사분면
                if (depth+j < inputN) and (i-j >= 0):
                    newlistN[depth +j][i-j]=1
                    flag = True
                    #2사분면
                if (depth-j >= 0) and (i+j < inputN):
                    newlistN[depth-j][i+j]=1
                    flag = True
                    #3사분면
                if (depth-j >= 0) and (i-j >= 0):
                    newlistN[depth-j][i-j]=1
                    flag = True
                    #4사분면
                if flag ==False:
                    break
                j= j+1

            solve(depth+1, newlistN)

        else:
            continue



count =0
inputN = int(input())
listN = [[0 for _ in range(inputN)] for _ in range(inputN)]
solve(0, listN)
print(count)
