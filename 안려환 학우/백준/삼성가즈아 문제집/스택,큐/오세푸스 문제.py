# n 명의 사람이 원을 이루면서 앉아있고 양의 정수 k(<= n) 가 주어진다. 
# 이제 순서대로 k번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 
# 계속해 나간다. 
# 이 과정은 n명의 사람이 모두 제거될 때까지 계속된다.
# 7, 3 인 오세푸스 순열은
# 3 6 2 7 5 1 4 이다.

# pop 이라는 것은 맨 오른쪽 끝에서 가져오는 동시에 삭제하는 것이다.
# pop은 그저 삭제하는 것이 아닌 값을 가져오는 동시에 삭제하는 것.

import sys

n,s = map(int,sys.stdin.readline().rstrip().split())
circle = [i for i in range(1, n + 1)]

# 인덱스값이랑 1차이나서 아예 그냥 s 를 1 줄여주는게 더 편하다.
num = s - 1
final = []

for i in range(n):
    if len(circle) > num:  # 그니까 반복수보다 큰 상태. 자꾸 빠져나가게 될 것이니 체크
        final.append(circle.pop(num)) # s 번째의 수를 꺼내서 저장한다.
        num += s - 1 # 이만큼 다음으로 이동해야 한다.
    else: # 이제 길이가 num이 같거나 커진 경우
        num = num % len(circle) # 다음 수로 넘기지 말고 그 나머지로 돌려서 한다.
        final.append(circle.pop(num)) # 예를 들어서 
        num += s - 1 # 이게 왜 num += num이 안먹히는지...
# 그 머냐

# 츨력 모양을 맞춰준다.
print("<", end='')
for i in final:
    if i == final[-1]:
        print(i, end = '')
    else:
        print(f"{i}, ", end='')
print(">")

