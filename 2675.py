from sys import stdin


inputN = int(stdin.readline())
result =""
for _ in range(inputN):
    first, second = map(str, stdin.readline().split(" "))
    for item in second.replace("\n", "") :
        for _ in range(int(first)):
            result = result + item
    print(result)
    result=""
