from sys import stdin

# https://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/

dict = ['0','A','B','C','D','E','F','G', 'H', 'I', 'J', 'K', 'L','N','M','O','P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
msg = input()

answer =[]
msgitem= msg
before=''
count=0
while True:
    print(msgitem)
    if msgitem in dict:
        # print(msgitem + "있다.")
        answer.append(dict.index(msgitem))
        count= count + len(msgitem)
        dict.append(msgitem + before)
        msgitem = msg[count:]

    else:
        if msgitem=='':
            break
        before= msgitem[-1]
        msgitem= msgitem[:-1]
    # else:
    #     answer.append(index(msgitem[0]))
    #     msgitem = msgitem[:lenth(1)]
    # if len(answer) ==len(msg):
    #     break


# print(dict)
print(answer)
