# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는
# 게임이다. 
# 숫자가 쓰인 카드들이 N * M 형태로 놓여있다. 이 때 N은 행의 개수 M은 열의 개수
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때 이후에 해당 행에서 가장 숫자가 낮은
# 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예시
# 2

# 입력 예시
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예시
# 3

# 그니까 각 행마다 가장 작은 수를 뽑아내서 그 수들 중에 가장 큰 수를 찾아내는 것이다.
# 저기 나열된 카드 중에 보면 1번 예시는 2 2 2 행의 2를 뽑아야 해서 2이고
# 2번 예시는 3 3 3 4의 3을 뽑아야 해서 3인 것이다.

import sys

n, m = map(int,sys.stdin.readline().split())
num_list = [0 for i in range(n)]
count_list = [0 for i in range(n)]

for i in range(n):
    num_list[i] = list(map(int,sys.stdin.readline().split())) # 아예 여기다가 sort하려했는데 안됩니다...


for i in range(n):
    num_list[i].sort() # 각 리스트들을 정렬해주었읍니다...

for i in range(n):
        count_list[i] = num_list[i][0] # 작은 값들을 따로 모읍니다...

count_list.sort()

print(count_list[-1]) # 정렬 후 가장 큰 값 뽑아냅니다..