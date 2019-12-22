import sys

def solve(a):

    if ((0((a % 4) == 0) and ((a % 100) != 0))) or ((a % 400) == 0):
        return "1"
    else:
        return "0"





if __name__ == "__main__":
    a = sys.stdin.readline()
    result = solve(int(a))
    print(result)
