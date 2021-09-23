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

test_case = int(sys.stdin.readline())
result_list = [0 for _ in range(test_case)]
stack = []
final = []
for i in range(test_case):
    n = int(sys.stdin.readline())
    stack.append(sys.stdin.readline().rstrip().split())
    for j in range(len(stack)):
        if j < max(stack):
            stack.append(stack.pop(j))
        else:
            final.append(st)