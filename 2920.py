from sys import stdin



listN = list(map(int, stdin.readline().split()))

checkpoint= 0


for i in range(8):
    if (listN[i+1] == (listN[i]-1)):
        checkpoint = 1
    elif (listN[i+1] == (listN[i]+1)):
        checkpoint = 2
    else:
        checkpoint = 3
        break
    if i == 6:
        break


if checkpoint == 1:
    print("descending")
elif checkpoint == 2:
    print("ascending")
else:
    print("mixed")
