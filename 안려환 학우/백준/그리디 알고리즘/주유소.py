import sys

n = int(sys.stdin.readline())

dis_list = list(map(int,sys.stdin.readline().split()))
coast_list = list(map(int,sys.stdin.readline().split()))
coast = 0
chippest = 0

dis_list.append(0)
for i in range(n):
    if i == 0 :
        coast += dis_list[i] * coast_list[i]
        chippest = coast_list[i]  # 가장 싼 값을 가지고 가면서 비교한다.
    else:
        if coast_list[i] < chippest: # 새로 최저가가 나타나면
            coast += dis_list[i] * coast_list[i]
            chippest = coast_list[i] # 그것으로 설정을 해준다.
        else:
            coast += dis_list[i] * chippest # 그렇지 않으면 기존 최저가로 

print(coast)