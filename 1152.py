from sys import stdin


inputline =list(stdin.readline().replace("\n", "").split(" "))

count = 0
for item in inputline:
    if item !='':
        count = count + 1
print(count)
