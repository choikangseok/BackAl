from sys import stdin

inputSTR = str(stdin.readline().replace('\n',''))

listN = ['c=','c-','dz=','d-','lj', 'nj', 's=', 'z=']
min=0
for item in listN:
    if item in inputSTR:
        inputSTR = inputSTR.replace(item, 'M')

print(len(inputSTR))
