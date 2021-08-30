import sys

insert_list = []
count_list = []
count_num = 0
for i in range(10):
    a = int(sys.stdin.readline())
    b = a % 42
    insert_list.append(b)
#여기까지 42로 나눈 나머지 수들을 모아서 리스트로 만들어주는 작업.
#set..... 이걸 사용해야하는군요...
count = len(set(insert_list))
print(count)
