# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 구하시오.
# 첫째 줄에 n(1<=n<=10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

import sys

user_input = int(sys.stdin.readline())

result = 0

for i in range(1, user_input+1):
    result += i

print(result)