from sys import stdin


testN = int(input())


for i in range(testN):
    str =''
    for j in range(i+1):
        str= str + '*'
    print(str)
