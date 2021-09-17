import sys


# . 처럼 아무 것도 없어도 균형잡힌 녀석이라고 할 수 있다.


# 일단 풀기 전에 이건 스택을 사용해야 하는 문제라고 한다
# 스택이란 제한적으로 접근할 수 있는 나열 구조이다. 
# 그 접근 방법은 언제나 목록 끝에서만 일어난다.
# 스택은 LIFO 라스트 인 퍼스트 아웃 그러니 탄창의 총알과 같이 마지막 
# 삽입한 것이 처음으로 나가게 되어있다.

# 문제는 .는 입력의 종료조건이다.
# stack 리스트를 만들어서 먼저 발생된 시작되는 괄호를 저장해주고
# 짝이 맞는 괄호가 생기면 pop 으로 리스트를 비워준다.
# 짝이 맞지 않는 괄호가 생기면 stack 리스트를 그대로 둔다.
# stack의 리스트가 비어있으면 yes를 출력하고 비어있지 않으면 no를 출력한다.
# - 짝이 지어졌으니 리스트가 비어진 것이라 yes가 나오면 된다.

# answer_list = []
# while True:
#     n = sys.stdin.readline()
#     stack = []

#     if n == '.':
#         break # 마침표가 오면 종료
    
#     for i in n:
#         if i == '[' or i == '(':
#             stack.append(i)
#         elif i == ']':
#             if len(stack) != 0 and stack[-1] == '[':
#                 stack.pop() # ]라는 짝이 왔을 때 꺼내서 비게 만든다. - 짝 맞추기 작업이다.
#             else:
#                 stack.append(']')
#                 break
#         elif  i == ')':
#             if len(stack) != 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(')') # 이걸 넣어줘야 리스트를 채워두어 이것이 균형이 맞지 않음을 알아챌 수 있다.
#                 break

#     if len(stack) == 0:
#         print('YES')
#     else:
#         print('NO')


# while True:
#     bracket = sys.stdin.readline().rstrip()
#     if bracket == ".":
#         break
#     bracket_stack = []
#     answer = True
    
#     for j in bracket:
#         if j == "(" or j == "[":
#             bracket_stack.append(j)
        
#         elif j == ")":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "(":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
                
#         elif j == "]":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "[":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break

#     if answer and not bracket_stack:  # 이 and not 연산은 둘 다 아니어야만 한다. 
#         print("YES")
#     else:
#         print("NO")


import sys
input = sys.stdin.readline
 
while True:
    s = input().rstrip()
    if s == '.':    # 종료 조건
        break
 
    stack = []
    flag = True    # 짝을 이루지 않는 경우
 
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
 
        elif stack and (s[i] == ')' or s[i] == ']'):  # stack은 있지만 닫힌 괄호가 나오는 경우
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:    # (])
                flag = False
 
        elif not stack and (s[i] == ')' or s[i] == ']'):  # stack이 없으면서 닫힌 괄호가 나오는 경우, )(
            flag = False
 
    if flag and not stack:
        print('yes')
    else:
        print('no')