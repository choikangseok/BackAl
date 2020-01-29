from sys import stdin

def solve(depth, result):
    global max
    global min
    if depth == inputN:
        if max <= result:
            max= result
        if min >= result:
            min= result

    newresult=0
    for i in range(len(listA)):
        k=listA.pop(i)
        if k == '+':
            newresult = result + listN[depth]
        if k == '-':
            newresult = result - listN[depth]
        if k == '*':
            newresult = result * listN[depth]
        if k == '/':
            if result < 0:
                result = -(result)
                result = result // listN[depth]
                newresult = -(result)
            else:
                newresult = result // listN[depth]

        solve(depth+1, newresult)
        listA.insert(i, k)
    return



max = -1000000000
min = 1000000000
inputN = int(input())
listN=list(map(int, stdin.readline().split(' ')))
listSA=list(map(int, stdin.readline().split(' ')))
SA = "+"*listSA[0] + "-"*listSA[1] + "*"*listSA[2] + "/"*listSA[3]
listA= list(SA)
solve(1, int(listN[0]))
print(max)
print(min)
#listSA[0] = + 개수
#listSA[1] = - 개수
#listSA[2] = x 개수
#listSA[3] = / 개수
