import sys 

# 이거 기호를 기준으로 나누는 것을 split 이옹
# 이게 식에서 이후 -가 더 나오더라도 +만으로 나누면 되는 것이
# -로 나누어진 애들을 싹 더해서 나중에 다 빼주면 되기 떄문.

# 그 +로 구분해서 나누는 것을 못했습니다....

a_list = list(map(str,sys.stdin.readline().rstrip().split('-'))) # rstrip 은 split 전에 개행을 제거하고 기준으로 구분한다. 말의 순서에 대해서 생각해보자.
# 개행은 그냥 무시해버리고 했는데 됩니다...
# 개행때문에 input쓰니 런타임 에러 발생
first_num = 0
else_num = 0

for i in a_list[0].split('+'): # 이 예외를 생각 못했읍니다.... 처음에 +가 나왔을 경우
    first_num += int(i)

for i in a_list[1:]: # 이런 방법을 생각 못하고 a_list 자체에서 split을 해주려 하니 오류
    for j in i.split('+'): # 이걸 못했습니다...
        else_num += int(j) 


print(first_num - else_num)