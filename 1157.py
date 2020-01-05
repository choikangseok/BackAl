from sys import stdin


testSTR= str(stdin.readline().replace("\n", ""))

listSTR = []
count = 0
bestcount = 0
BestM =''
flag= 0

for item in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for testItem in testSTR:

        if (testItem == item) or (testItem == item.upper()):
            count = count + 1
    if bestcount == count:
        flag = 1
    if bestcount < count:
        bestcount = count
        BestM = item.upper()
        flag = 0
print(bestcount)
if flag == 0 :
    print(BestM)
else:
    print("?")
