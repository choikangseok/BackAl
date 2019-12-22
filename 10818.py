from sys import stdin


a = int(stdin.readline())

listN = list(map(int, stdin.readline().split()))

listN.sort()

print("%s %s" % (listN[0], listN[-1]))
