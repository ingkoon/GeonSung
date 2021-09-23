import sys

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍으로 표현된다. 
# 그니까 () 이렇게 붙은 것에서만 레이저가 나오는 것이다.
# 쇠막대기의 왼쪽 끝은 여는 괄호 오른쪽 끝은 닫는 괄호로 표현된다.

# 그래서 이렇게 잘렸을 때의 쇠막대기의 개수를 구하는 프로그램을 작성하라


# 쇠막대기가 잘리기 위한 조건
# 레이저 시작점보다 막대기 시작점이 작거나
# 레이저 시작점보다 막대기 끝나는 점이 커야 잘린다.

# input_value = str(sys.stdin.readline().rstrip())
# stick_list = []
# lazer_list = []

# for i in range(len(input_value)):
#     if input_value[i] == '(':
#         if input_value[i + 1] == ')':
#             stick_list[i][0]
            
# 풀이
# (이 나올 경우 stack에 push한다.
# )이 나올 경우 그 전 문자열이 )일 경우 막대기가 있는 것이므로 stack에서 1개를 pop 하고
# 스택의 크기만큼 result에 더한다. -> 이걸 이해 못하겠네 스택 크기면 길이만큼인데 그걸 왜 더해주는거지....?
# 잘린 쇠 막대 수를 구해야하니 더하는건지...
# )이 나올 경우 그 전 문자열이 )일 경우 막대기가 있는 것이므로 stack 에서 1개를 pop하고 
# result에 1을 증가시킨다.

# 이해
# 열린 괄호일 경우 일단 스택에 다 넣고
# 닫힌 괄호중 이전이 열린거면 레이저 - 스택 길이만큼 더해준다. 
# 아 이 막대기들이 동강이 나면서 있는 수만큼 더 더해지니까
# 그리고 레이저 아니라면 result에 하나 더 더해주는데
# 최종 쇠막대기 수를 구하는 것이니 막대가 하나 추가된 격인 것이다.

import sys

input_list = sys.stdin.readline().rstrip()

stack = []
result = 0

for i in range(len(input_list)):
    if input_list[i] == '(':
        stack.append('(') # stack 에 ( 자체를 넣어준다. 

    else:
        if input_list[i - 1] == '(': # 이전 것이 (라면 차피 처음은 (로 시작한다.
            stack.pop()
            result += len(stack) # 레이저라서 이 스택의 길이만큼이 더 생긴 것이다.
        else:
            stack.pop() # 잘린 것이라 꼭 pop연산을 해주면서 수를 세준다.
            result += 1

print(result)