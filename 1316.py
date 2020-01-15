from sys import stdin

a= int(stdin.readline())

listN = []
for _ in range(a):
    listN.append(str(stdin.readline().replace('\n','')))

output=0
flag=0
count=0
for listItem in listN:
    count=0
    for alphabet in 'abcdefghijklmnopqrstuvwxyz':
        flag=0
        for i in range(len(listItem)):
            if alphabet == listItem[i]:
                count = count+1
                flag=1
            if (flag == 1) and (alphabet != listItem[i]):
                break
    if count == len(listItem):
        output= output + 1
print(output)
