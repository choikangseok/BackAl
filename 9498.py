import sys

def solve(a):
    if a < 60:
        return "F"
    elif a < 70:
        return "D"
    elif a < 80:
        return "C"
    elif a < 90 :
        return "B"
    else:
        return "A"



if __name__ == "__main__":

    a = sys.stdin.readline()

    result = solve(int(a))
    print(result)
