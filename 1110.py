from sys import stdin



num1 = int(input())
i = 0
NEWnumber = num1
while True:
    i= i+1
    NEWnumber = (((NEWnumber/10) + (NEWnumber % 10))%10) + (NEWnumber % 10)*10
    if NEWnumber == num1:
        print(i)
        break
