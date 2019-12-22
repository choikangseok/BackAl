from sys import stdin


testN = int(input())


for i in range(testN):
    str =''
    for _ in range(testN-(i+1)):
        str = str + ' '
    for _ in range(i+1):
        str =  str +'*'
    print(str)
