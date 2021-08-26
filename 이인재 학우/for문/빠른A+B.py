# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1000 이하이다.
# 각 테스트케이스마다 A+B를 한줄에 하나씩 순서대로 출력한다.

import sys

userInput = int(sys.stdin.readline())

for i in range(userInput):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)