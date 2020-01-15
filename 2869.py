from sys import stdin
import math

A, B, V = map(int,stdin.readline().split())



# total=0
day= math.ceil((V-A)/(A-B)) + 1
print(int(day))
# while True:
#     total = total + A
#     if total == V:
#         print(day)
#         break
#     total = total - B
#     day= day + 1
