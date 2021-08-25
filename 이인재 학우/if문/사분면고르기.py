import sys

# 두 줄에 걸쳐 각각의 정수 입력
inputA = int(sys.stdin.readline())
inputB = int(sys.stdin.readline())

# 각각의 조건에 맞게 출력될 수 있도록 지정
if inputA > 0 and inputB >0:
    print(1)
elif inputA < 0 and inputB >0:
    print(2)
elif inputA < 0 and inputB <0:
    print(3)
else:
    print(4)
