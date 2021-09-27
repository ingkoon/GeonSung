# 정수를 구현하는 큐를 구현한 다음 입력으로 주어지는 명령을 처리하는 프로그램을
# 작성하시오
# push x 정수 x를 큐에 넣는 연산이다.
# pop 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는
# -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
check = sys.stdin
n = int(check.readline().rstrip())

que = deque()

for _ in range(n):
    input_word = check.readline().rstrip().split()
    zero = input_word[0]
    if len(input_word) == 2:
        que.append(input_word[1])
    elif len(input_word) == 1:
        if zero == 'pop':
            if len(que) == 0:
                print(-1)
            else:
                print(que.popleft())
        elif zero == 'size':
            print(len(que))
        elif zero == 'empty':
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif zero == 'front':
            if len(que) == 0:
                print(-1)
            else:
                print(que[0])
        elif zero == 'back':
            if len(que) == 0:
                print(-1)
            else:
                print(que[-1])

# deque 를 이용하니 매우 쉽게 해결을 하였읍니다...