# from sys import stdin
#
# inputN = int(stdin.readline())
# listN = list()
# for _ in range(inputN):
#     item = stdin.readline().replace("\n","")
#
#     if item not in listN:
#         listN.append(item)
# listN.sort(key= lambda x : (len(x), x))
#
# for item in listN:
#     print(item)
from sys import stdin

inputN = int(stdin.readline())
listN = list()
for _ in range(inputN):
    item = stdin.readline().replace("\n","")
    listN.append(item)
listN = list(set(listN))
listN.sort(key= lambda x : (len(x), x))

for item in listN:
    print(item)
