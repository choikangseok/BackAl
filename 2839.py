from sys import stdin

inputN = int(input())
i=0
t=0
x=0
y=-1

while True:
    if(5*i > inputN):
        break
    if (inputN-5*i)%3 == 0:
        x= i
        y= (inputN-5*i)/3
    i= i+1
print(int(x+y))
