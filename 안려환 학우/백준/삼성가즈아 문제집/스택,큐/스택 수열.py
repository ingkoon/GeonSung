# 그니까 이놈이 하고싶은게 스택은 LIFO 이다. 나중에 들어간게 먼저 나오는
# 권총 탄창과 같이 작동을 한다.
# 1부터 n까지 수를 일단 다 넣는다. 이 때 스택에 push하는 순서는 반드시 오름차순을
# 지키도록 한다.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라
# 풀어서 쓰면 일단 다 넣고 
# 8 4 3 6 8 7 5 2 1 이면 8은 갯수니까 빼고 나머지 43687521을 이용해서 
# 먼저 스택에 넣어주기 위해 

import sys
n = int(sys.stdin.readline())

count = 0 # 스택에 넣어줄 값
stack = []
final = []
possitive = True

for i in range(n):
    x = int(sys.stdin.readline())
    
    while count < x:
        count += 1 # 차피 오름차순으로 집어넣을 것이기 때문이다.
        stack.append(count) # 스택에 push 해준다.
        final.append("+")

    if stack[-1] == x: # 스택의 최대 값이 x와 비교해서 같으면 
        stack.pop() # 스택에서 pop 연산을 해준다. 마지막 값을 꺼내주어야 하기 때문이다.
        final.append("-") # 스택서 빠져서 최종으로 갔기 때문에

    else:
        possitive = False # pop 도 push도 못하는 상황이면
        break # break로 아예 끝내버려도 된다.

if possitive == False:
  print("NO")
else:
  print("\n".join(final))