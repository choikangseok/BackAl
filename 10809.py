from sys import stdin


result =""
stringS = str(stdin.readline().replace("\n",""))

for item in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for item2 in stringS:
        if item == item2:
            result= result + str(count) + " "
            break
        count = count + 1
    else:
        result= result + "-1 "
print(result)
