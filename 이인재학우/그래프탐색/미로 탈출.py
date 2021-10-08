# 미로 탈출
# 문제
# N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 
# 현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 
# 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
# 미로는 반드시 탈출할 수 있는 형태로 제시된다. 
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력
# 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 
# 다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다. 
# 각각의 수들은 공백 없이붙어서 입력으로 제시된다. 
# 또한 시작 칸과 마지막 칸은 항상 1이다.

# 출력
# 첫째 줄에 최소 이동 칸의 개수를 출력한다.

# 입력 예시

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시

# 10

import sys
from collections import deque

# 맵의 크기 입력
n, m = map(int, sys.stdin.readline().split())

# 맵 내부 요소 입력
graph = [[] for i in range(n)]

# for문을 통해 각각의 요소 입력
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

# 이동 거리에 대한 배열 요소 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# BFS를 통해 지정
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        # 큐에서 각각의 값을 꺼내온다
        x, y = queue.popleft()

        # 다음 x, y의 값을 가져온다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 크기에서 벗어날 경우 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 갈 수 없는 지점일 경우 continue
            if graph[nx][ny] == 0:
                continue
            
            # 갈수 있을 경우 해당 위치에 이동 거리를 1추가시켜 누적시킨 값을 할당한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # 다음 x, y값을 가져와 반복 수행
                queue.append((nx, ny))

    # 최종값 -1 한 값을 가져온다
    return graph[n-1][m-1]

# 반복 수행한 값을 출력
print(bfs(0, 0))

