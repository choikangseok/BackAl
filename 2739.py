from sys import stdin



user_input = stdin.readline().split()


a = int(user_input[0])



for i in range(9):
    print("%s * %s = %s" % (a, i+1, (i+1)* a))
