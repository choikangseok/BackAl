from sys import stdin



user_input  = stdin.readline().split()



hour = int(user_input[0])
min = int(user_input[1])


if min < 45 :
    hour = hour - 1
    min = 60 + min - 45
    if hour < 0:
        hour =23
else:
    min = min - 45


print(str(hour) + " " + str(min))
