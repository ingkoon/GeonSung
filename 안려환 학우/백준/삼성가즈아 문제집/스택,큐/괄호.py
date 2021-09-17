import sys

n = int(sys.stdin.readline())


# def a_check(input_list, count):
#     while input_list[i] == '(':
#         count += 1

# def b_check(input_list, count):
#     while input_list[i] != '(':
#         count += 1

# input_list = [0 for _ in range(n)]
# answer_list = [0 for _ in range(n)]
# for i in range(n):
#     input_list[i] = map(str,sys.stdin.readline().rstrip().split())
# for j in range(len(input_list[i][j])):
#         if input_list[i][j] != '(':
#             answer_list[i] = 'NO'
#         else:
#             while a_count != 0 or b_count != 0: # 원래는 while문 안에 함수들을 넣어주는 방식으로
#                 a_count = a_check(input_list[i][j],count) #풀이를 하려 했으나 실패했읍니다...
#                 b_count = b_count(input_list[i][j + a_count],count)
#                 if a_count == b_count:
#                     answer_list[i] = 'YES'
#                 else:
#                     answer_list[i] = 'NO'

# for i in range(n):
#     print(answer_list[i])

# 리스트 안에 리스트를 만드는 것이 아닌 ( 가 나오면 1 더해주고 ) 나오면 1을 뺴주는 식으로
# 0나오면 YES가 되는 방식이다.....



answer_list = [0 for _ in range(n)]
for i in range(n):
    input_list = list(map(str,sys.stdin.readline().rstrip()))
    sum = 0  # 이걸 초기화시켜줘야할걸 계속 빼둬서 그 어떤 YES도 꺼내지 못한 문제 발생
    for j in input_list:
        if j == '(':
            sum += 1
        elif j == ')':
            sum = sum - 1 # 이 if 문을 나간 후
        if sum < 0: # sum이 0보다 작다는건 )가 더 많다.
            answer_list[i] = 'NO'
            break
    if sum > 0: # (가 더 많은 경우에도 아니다.
        answer_list[i] = 'NO'
    elif sum == 0:
        answer_list[i] = 'YES'

for i in range(n):
    print(answer_list[i])



