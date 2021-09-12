# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나눠 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 예를 들어 N이 17 K가 4라고 가정한다. 1번 하면 N은 16된다. 이후 2번 과정을 2 번 수행하면
# N은 1이 된다. 결과적으로 이 전체 과정을 실행한 횟수는 3이 된다.
# 이 최소 횟수를 구하자.
# 입력 예시
# 25 5
# 출력 예시 
# 2

import sys
n, k = map(int,sys.stdin.readline().split())
count = 0

def call_back(n, k, count):
    while n != 1:
        if n % k == 0:  # 나눠지는걸 항상 먼저 해야합니다... 그래야 최소가 됩니다..
            n = n // k
            count += 1

        else:
            n -= 1
            count += 1
            call_back(n,k,count) # 이번엔 재귀라는 것을 이용해보았읍니다...

    if n == 1:
        return count # return을 해주어야 마무리가 됩니다... 프린트는 n이 1일 때 실행되니 두 번이 됩니다.

print(call_back(n, k, count))



