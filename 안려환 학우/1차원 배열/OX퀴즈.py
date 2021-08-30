import sys

test_results = [] #이건 ox를 담기 위함
sum = 0  #그 때 그 때의 1을 위함
total_sum = 0  #모든 더함들을 합해서 리스트에 넣어주기 위해
total_list = []  #마지막 출력을 위한 리스트

N = int(sys.stdin.readline())
for i in range(N):
    insert_answer = sys.stdin.readline() #이것도 그냥 그대로 입력을 받기
    for i in insert_answer:   #이게 참 어려웠다. 입력받은 문자열 안에서 비교
        if i == 'O':
            sum += 1
        else:
            sum = 0 #이래야 중첩되는 덧셈을 막을 수 있다.
        total_sum += sum
    total_list.append(total_sum)
    sum = 0  #계속 초기화를 시켜줘야 다음 입력받을 문제들이 새로 채점된다.
    total_sum = 0

for i in range(len(total_list)):
    print(total_list[i])

#머리 깨질뻔~