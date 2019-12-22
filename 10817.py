from sys import stdin




user_input = stdin.readline().split()


a =int(user_input[0])
b =int(user_input[1])
c =int(user_input[2])


if a >= b:
    if b >= c:
        print(b)
    elif a >= c:
        print(c)
    else:
        print(a)
else:
    if a >= c:
        print(a)
    elif b >= c:
        print(c)
    else:
        print(b)
