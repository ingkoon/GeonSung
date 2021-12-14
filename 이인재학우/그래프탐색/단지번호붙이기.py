# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys

n = int(sys.stdin.readline())

mapArr = [[] for i in range(n)]

cntArr = []
for i in range(n):
    mapArr[i] = list(map(int, sys.stdin.readline().rstrip()))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
        
    if mapArr[x][y] == 1:
        global cnt
        cnt += 1
        mapArr[x][y] = 0     

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

result = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if  dfs(i,j) == True:
            result += 1
            cntArr.append(cnt)
            cnt = 0



    
print(result)

cntArr.sort()

for i in cntArr:
    print(i)
