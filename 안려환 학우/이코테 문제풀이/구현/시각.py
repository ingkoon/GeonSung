# 정수 n이 입력되면 0시0분0초부터 n시 59분 59초까지 모든 시각 중에서
# 3이 하나라도 추가된 모든 경우의 수를 구하는 프로그램 만들어라
# 입력
# 5
# 출력
# 11475

import sys

n = int(sys.stdin.readline())
count = 0

# 두 숫자를 str으로 바꿔서 if 3 in str(i) 하면 count를 하나 올려주는
for i in range(n+1): # 아 n시 59분 59초까지의 경우를 못더해줬읍니다...
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(k) or '3' in str(j): # 아 책에서는 이 str들을 다 더해줘서 이렇게 하나하나 안써주어도 되었읍니다....
                count += 1

print(count)