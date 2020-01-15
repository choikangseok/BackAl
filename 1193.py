from sys import stdin


inputnum = int(stdin.readline())
count =1
n=0
flag = True
while ((n+n*n)/2) < inputnum:
    n= n+1
    flag = not flag
K= n-1

if flag == True:
    startb= n +1 -(inputnum - (K+K*K)/2)
    starta= n +1 -startb
else:
    starta= n +1 -(inputnum - (K+K*K)/2)
    startb= n +1 -starta
print(str(int(starta))+"/"+str(int(startb)))
# b=1
# flag= 0
# count = 1
# while True:
#     if count == inputnum :
#         break
#     if flag == 0 :
#         count = count + 1
#         b= b+1
#         if count == inputnum:
#             break
#         inita=a
#         initb=b
#         while True:
#
#             count = count + 1
#             a= a+1
#             b= b-1
#             if inita==b and initb==a:
#                 break
#             if count == inputnum:
#                 break
#         flag = 1
#     elif flag == 1 :
#
#         a= a+1
#         count = count + 1
#         if count == inputnum:
#             break
#         inita=a
#         initb=b
#         while True:
#             count = count + 1
#             a= a-1
#             b= b+1
#             if inita==b and initb==a:
#                 break
#             if count == inputnum:
#                 break
#         flag = 0
# print(str(a) + "/" + str(b))
