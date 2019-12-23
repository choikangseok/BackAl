from sys import stdin

listN=[]
for i in range(10):
    listN.append(int(stdin.readline()) % 42)

s1 = set(listN)

print(len(s1))
