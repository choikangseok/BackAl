from sys import stdin

def solve(x, y, depth):
    initx = x
    inity = y
    depth = depth + 1
    if linstN[y][x+1] != '#':
        while True:
            # 좌
            if listN[x+1][y] == '#':
                break
            else:
                x=x+1
        #좌로 가는 경우
    x= initx
    y= inity
    if linstN[y][x-1] != '#':
        while True:
            if listN[x-1][y] == '#':
                break
            else:
                x=x-1
        #우로 가는 경우
    x= initx
    y= inity
    if linstN[y+1][x] != '#':
        while True:
            if listN[x][y+1] == '#':
                break
            else:
                y=y+1
        #상으로 가는 경우
    x= initx
    y= inity
    if linstN[y-1][x] != '#':
        while True:
            # 하
            if listN[x][y-1] == '#':
                break
            else:
                y=y-1
        #하로 가는 경우

a, b = map(int, stdin.readline().split())
listN= list()

for i in range(a):
    listN.append(list(map(str, stdin.readline().replace('\n',''))))
    if 'O' in listN[i]:
        # print(listN[i])
        x=listN[i].index("O")
        y=i
depth =0
listD= list()
listD.append([depth, x, y])
print(listD)
while True:
    if depth <10:
        break
    initx = x
    inity = y
    depth = depth + 1
    if listN[y][x+1] != '#':
        while True:
            # 좌
            if listN[x+1][y] == '#':
                break
            else:
                x=x+1
        listD.append(depth,x,y)
        #좌로 가는 경우
    x= initx
    y= inity
    if listN[y][x-1] != '#':
        while True:
            if listN[x-1][y] == '#':
                break
            else:
                x=x-1
        #우로 가는 경우
    x= initx
    y= inity
    if listN[y+1][x] != '#':
        while True:
            if listN[x][y+1] == '#':
                break
            else:
                y=y+1
        #상으로 가는 경우
    x= initx
    y= inity
    if listN[y-1][x] != '#':
        while True:
            # 하
            if listN[x][y-1] == '#':
                break
            else:
                y=y-1

else:
    print('-1')

#
# for i in range(10):
#     result =
#
#     if result == 'R':
#         print(i)
# else:
#     print("-1")
