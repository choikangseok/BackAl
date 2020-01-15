from sys import stdin

inputN = int(input())

stri = str(inputN)

# for k in stri:
#     print(k)
for i in range(1, inputN-1):
    stri = str(i)
    BH_hap = 0
    for k in stri:
        BH_hap = BH_hap + int(k)
    BH_hap = BH_hap + i
    if inputN == BH_hap:
        print(i)
        break
else:
    print("0")
