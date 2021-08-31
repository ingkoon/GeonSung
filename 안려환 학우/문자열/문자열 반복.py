import sys

T = int(sys.stdin.readline())
total_list = []
total_str = ''

for i in range(T):
    num, S = sys.stdin.readline().split(" ")   #입력받기 방법
    final = S.rstrip()  #자꾸 개행문자가 붙어서 빼주는 작업을 했다.
    for j in final:
        total_str += int(num) * j #문제에서 원하는 반복
    total_list.append(total_str)  #최종 출력할 리스트에 더해준다.
    total_str = '' #이거 안해주면 계속 뒤로 붙는다.


for i in range(T):
    print(total_list[i])