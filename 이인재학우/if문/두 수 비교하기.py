import sys

# 두 정수 입력 및 분할
a, b = map(int, sys.stdin.readline().split())

# if 문을 통한 비교 수행
if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")