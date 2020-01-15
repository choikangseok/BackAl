from sys import stdin
import math

inputnum = int(input())

h= list()
w= list()
n= list()

for _ in range(inputnum):
    H, W, N = map(int, stdin.readline().split())
    h.append(H)
    w.append(W)
    n.append(N)

for i in range(inputnum):
    XX=math.ceil(n[i]/h[i])
    if XX <10:
        strXX = "0"+str(XX)
    else:
        strXX = str(XX)
    if n[i]%h[i] ==0:
        YY= h[i]
    else:
        YY= n[i]%h[i]
    print(str(YY)+strXX)
