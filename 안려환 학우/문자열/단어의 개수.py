import sys

count = 0
str_list = list(sys.stdin.readline().strip().split(" "))
if len(str_list) == 1:
    if str_list[0] == '': #이게 아무 것도 안써진 것도 인식해서 이 조건문으로
        print(0) #들어오지 않았다..
    else:
        print(1) #여기 예외처리를 안해줘서 자꾸 틀렸다.
    for i in str_list:
        if i != '':
          count += 1  
    print(count)


#사막의 오아시스같은 개꿀문제인줄 알았는데 신기루였읍니다.....
#너무 틀려서 찾아보니 그냥 공백인 경우를 깜빡하였읍니다...


