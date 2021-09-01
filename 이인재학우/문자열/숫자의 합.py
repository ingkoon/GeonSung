# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 입력으로 주어진 숫자 N개의 합을 출력한다.cnt_input = int(input())

import sys

# 숫자를 문자열 타입으로 입력
num_input = sys.stdin.readline()
num_input = num_input[:-1]
# 결과값을 위한 변수 선언
result = 0

# 반복문을 통해 문자열에서 숫자를 하나씩 꺼내와 정수 변환 후 출력
for i in num_input:
    result += int(i)

# 결과 출력
print(result)