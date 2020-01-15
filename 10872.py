from sys import stdin

def factorial(n):

    if n>1:
        return n*factorial(n-1)
    else :
        return 1



numN = int(input())

print(factorial(numN))
