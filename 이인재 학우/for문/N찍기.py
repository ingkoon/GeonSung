# 자연수 N이 주어졌을 때, 1부터 N까지 한줄에 하나씩 출력하는 프로그램을 작성하시오
# 첫째 줄에 10,000보다 작거나 같은 자연수 n이 주어진다.
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

import sys

userInput = int(sys.stdin.readline())

for i in range(1,userInput+1):
    print(i)
