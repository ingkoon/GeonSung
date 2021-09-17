# n * n 크기의  정사각형 공간 안에 있다.
# 이를 이용하여 LRUD 좌우상하 라는 입력 값이 나타나고
# 그렇게 입력받은만큼 이동이 일어난다.
# 지도 밖으로 나가는 이동은 무시된다.
# 출력은 이동 후 최종 위치를 반환한다.

import sys


n = int(sys.stdin.readline())
directions = ['L', 'R', 'U', 'D']
moves = [-1, 1, -1, 1] # 위 아래 살짝 헷갈렸읍니다...
now = [1,1]


input_list = str(sys.stdin.readline().rstrip().split())
# 입력부를 구현해주었습니다.


for i in input_list:
    for j in range(len(directions)):
        if i == directions[j]:
            if now[0] + moves[j] <= 0 or now[1] + moves[j] <= 0:  # 지도 밖으로 나가는 경우 제외해준다.
                continue # 이 제외를 위한 continue 를 해준 것이다.
            else:
                if j > 1:
                    now[0] += moves[j] # y축 이동에 대한 것
                else:
                    now[1] += moves[j] # x축 이동에 대한 것

                    
# 책에서는 제가 지도 밖으로 나가는 경우에 대해서 안쪽 반복문 밖에 선언하여 
# 저보다 실행속도가 더 빠르게 하였읍니다....
# 저는 매번 이 움직임이 지도 밖으로 나가는 경우에 대해서 잡아줘야할 것 같다고 생각해서
# 안쪽 포문에 조건을 넣어 주었읍니다....
print(now)