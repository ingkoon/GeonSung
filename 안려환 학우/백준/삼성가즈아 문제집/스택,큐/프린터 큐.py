import sys

# 프린터기는 FIFO에 따라 인쇄가 진행된다. 여러 개의 문서가 쌓인다면
# QUEUE 자료구조에 쌓여서 FIFO에 따라 인쇄가 된다.
# 가장 앞에 있는 문서의 중요도 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
# 이 문서를 인쇄하지 않고 QUEUE의 가장 뒤에 재배치한다. 그렇지 않다면 바로 인쇄

# ex)
# A B C D 
# 2 1 4 3 
# 이렇게 중요도라면 
# C D A B 순서대로 출력을 하게 된다.
# 중요도라는 수가 높을수록 먼저 인쇄하는 것
# 중요도 보면 2는 뒤에 4,3 있어서 맨 뒤로 가고
# 1은 당연히 맨 뒤로 가고
# 4는 바로 인쇄
# 3인쇄 후 2 1 인쇄 이렇게 간다.

# 뒤에 본인보다 중요도 큰 수 있으면 바로 맨 뒤로 간다.

from collections import deque

num = int(sys.stdin.readline())
final = []
for _ in range(num):
    N, M = map(int,sys.stdin.readline().split())
    que = deque(map(int,sys.stdin.readline().split()))
    cnt = 0
    while que:
        top = max(que) # 최대와 비교
        M -= 1 # 몇 번째 자리의 수를 가져다 쓸 것인지인 M
        pop = que.popleft() 
        if top != pop:
            que.append(pop) # 내가 사용했던 것을 좀 더 보기 편하게 만들었다.
            if M < 0:
                M = len(que) - 1
        else:
            cnt += 1
            if M == -1:
                final.append(cnt) # 출력부 모양을 맞춰주기 위함이다.
                break

for i in final:
    print(i)

# test_case = int(sys.stdin.readline())
# result_list = [0 for _ in range(test_case)]
# stack = []
# final = []
# for _ in range(test_case):
#     n, s = map(int,sys.stdin.readline().rstrip().split())
#     temp = [i for i in range(1,n + 1)]
#     stack = sys.stdin.readline().rstrip().split()
#     for j in range(len(stack)):
#         if stack[j] < max(stack):
#             stack.append(stack.pop(j))
#             temp.append(temp.pop(j))
#         else:
#             stack.pop(j)
#             final.append(temp.pop(j))

