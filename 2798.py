from sys import stdin
#
# N, M = map(int, stdin.readline().split())
# listN = list(map(int,stdin.readline().split(' ')))
#
#
# result=0
# for i in range(len(listN)-2):
#     for j in range(len(listN)-i-2):
#         j= i + j+ 1
#         for k in range(len(listN)-j-1):
#             k = k + j + 1
#             if (listN[i] + listN[j] + listN[k]) <= M  and (listN[i] + listN[j] + listN[k] > result):
#                 result = listN[i] + listN[j] + listN[k]
# print(result)

N, M = map(int, stdin.readline().split())
listN = list(map(int, stdin.readline().split(' ')))

result=0

for i in range(len(listN)-2):
    for j in range(i+1,len(listN)-1):
        for k in range(j+1,len(listN)):
            if listN[i] + listN[j] + listN[k] <= M  and listN[i] + listN[j] + listN[k] > result:
                result = listN[i] + listN[j] + listN[k]

print(result)
