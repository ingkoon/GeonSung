import sys

T = int(sys.stdin.readline())

count = 0
move = 1 # 처음엔 -1 0 1 이니 1로 확정이기 때문이다.
final_move = 0

for _ in range(T):
    x, y = map(int,sys.stdin.readline().split(" "))

    distance = y - x #이걸 생각못했다.
    
    while final_move < distance:
        count += 1
        final_move += move # 움직인만큼 더해준다. 앞으로 증가하는 양은 움직인 것에서 1 더
        if count % 2 == 0: #이게 도착하기 하나 전일땐 1칸만 움직여서 직전에서 하나 움직여야
            move += 1
    print(count)

# 이것도 틀렸다고 한다. 다른 어려운 풀이를 보고 이해중에 있읍니다....
