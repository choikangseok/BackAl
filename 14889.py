from sys import stdin
sum_start=0
sum_link=0
sub_sum=10000
def solve(depth, st):
    global sum_start
    global sum_link
    global sub_sum
    
    if depth ==inputN/2:
        list_link=list(set([i for i in range(1,inputN+1)]) - set(list_start))
        # print("listN--start")
        # print(list_start)
        # print("listN--link")
        # print(list_link)
        for i in range(len(list_start)-1):
            for j in range(i+1, len(list_start)):
                sum_start = sum_start + listN[list_start[i]-1][list_start[j]-1] + listN[list_start[j]-1][list_start[i]-1]
                # print(listN[list_start[i]-1][list_start[j]-1])
                # print(listN[list_start[j]-1][list_start[i]-1])

        for i in range(len(list_link)-1):
            for j in range(i+1, len(list_link)):
                sum_link = sum_link + listN[list_link[i]-1][list_link[j]-1] + listN[list_link[j]-1][list_link[i]-1]
                # print(listN[list_link[i]-1][list_link[j]-1])
                # print(listN[list_link[j]-1][list_link[i]-1])

        if sub_sum > abs(sum_start-sum_link):
            sub_sum = abs(sum_start-sum_link)
            # print(sub_sum)
        sum_start=0
        sum_link=0
        return

    for k in range(st, inputN+1):
        list_start.append(k)
        solve(depth+1, k+1)
        list_start.pop()
        if list_start == []:
            return



inputN = int(input())
listN = []
for _ in range(inputN):
    listN.append(list(map(int, stdin.readline().split(' '))))
list_start = []

solve(0, 1)
print(sub_sum)
