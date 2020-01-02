from sys import stdin


testN = int(stdin.readline())
answer = []
#.replace("\n","") 굳이 안넣어줘도 된다. readline()에

#여기엔 엄청난 꿀팁이 있다.
# sum에서 sum(listN[1:]) 이렇게 하면 1~쭉 다더해준다.
for _ in range(testN):
    listN = list(map(int, stdin.readline().split()))
    #sum=0.0
    sumt = sum(listN[1:])
    # for i in range(int(listN[0])):
    #     sum= sum + listN[i+1]
    average= sumt / float(listN[0])
    Tperson=0.0
    for k in range(int(listN[0])):
        if average < listN[k+1]:
            Tperson=Tperson+1.0
    result = Tperson / float(listN[0])
    answer.append("%0.3f" % (result*100))
for item in answer:
    print(item+"%")
