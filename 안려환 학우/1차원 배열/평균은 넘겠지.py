import sys

N = int(sys.stdin.readline())
scores_list = []
final_list = []
count = 0
sum = 0
avr = 0

for i in range(N):
    scores_list += map(int,sys.stdin.readline().split(" "))
    if len(scores_list) != scores_list[0] + 1: #맨 앞의 수와 동일하지 않다면
        print("You entered wrong nums")
    else:
        for i in range(1,scores_list[0] + 1):  #가장 마지막 수까지 더해주기 위해 +1
            sum += scores_list[i]
        avr = sum / scores_list[0]

        for i in range(1,scores_list[0] + 1):
            if scores_list[i] > avr:
                count += 1
        
        final = count / scores_list[0] * 100
        final_list.append(final)
        final = 0
        count = 0 #카운트 초기화
        sum = 0 # +=로 해놔서 초기화해줘야 한다.
        scores_list.clear() #초기화안해주면 뒤로 밀린다.

for i in range(N):
    print(str('%.3f' % round(final_list[i], 3)) + '%')