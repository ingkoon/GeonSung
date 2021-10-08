# N*M 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 떄 생성되는 총 아이스크리므이 개수를 구하는 프로그램을 작성 하시오.
# 다음의 4*5얼음 틀 예시 에서는 아이스크림이 총 3개 생성된다.

# 00110
# 00011
# 11111
# 00000

# 입력 조건
# 첫 번째 즐에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다.
# 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

# 출력 조건
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

import sys

# 얼음 틀의 크기 입력
n, m = map(int, sys.stdin.readline().split())

# DFS를 수행하기 위한 그래프 선언
graph = [[] for i in range(n)]

# 그래프 내에 얼음이 차는곳 지정
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

# dfs
def dfs(x, y):

    # 얼음 틀을 벗어나면 False 반환
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 얼음이 있는 부분은 1로 변경
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상하좌우에 맞게 이동
        dfs(x - 1,y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        # True 반환
        return True
    # 얼음이 탐지되지 않았을 경우 False반환
    return False

# 결과를 반환하기 위한 변수 선언 및 할당
result = 0

# n * m사이즈에 맞게 수행 후 결과 반환
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1 

# 결과 출력
print(result)