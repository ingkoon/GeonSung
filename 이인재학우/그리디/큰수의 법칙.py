# 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), k(1 <= K <= 1,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 1,000 이하의 수로 주어진다
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 첫째 줄에 동빈이의 큰수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력예시
# 46

import sys

# 각각의 변수 할당
n, m, k = map(int, sys.stdin.readline().split())

# 전체 값을 리스트 타입으로 할당
arr = list(map(int, sys.stdin.readline().split()))

# 정렬
arr.sort()

# 최댓값과 그다음 최댓값을 리스트에서 추출
max_value1 = arr[-1]
max_value2 = arr[-2]

# 카운트 변수와 결과 출력을 위한 변수 선언
cnt = 0
result = 0

# m번만큼의 덧셈을 할 것이기 때문에 m번 만큼의 반복 수행
for i in range(m):
    # cnt변수가 k와 같을 경우 두번째 최댓값을 더하고 cnt를 0으로 초기화
    if cnt == k:
        result += max_value2
        cnt = 0
        continue
    # 그 이외의 경우에는 최댓값을 더한다
    result += max_value1
    cnt += 1

# 결과 출력
print(result)

