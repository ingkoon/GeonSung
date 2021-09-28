from sys import stdin
from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 이런 식으로 나오게 되면 BFS를 써야 한다는 것을 알아두면 좋은 것 같다.

#BFS 소스코드 구현
def BFS(x, y):
    que = deque()
    que.append((x,y))
    while que:
        x, y = que.popleft()
        for i in range(4): # 네 방향이기에
            nx = x + dx[i] # 각 방향으로의 이동이다.
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 밖으로 벗어나면 안된다.
                continue
            if graph[nx][ny] == 0: # 벽인 경우이다.
                continue
            if graph[nx][ny] == 1: # 갈 수 있는 길이면 
                graph[nx][ny] = graph[x][y] + 1 
                que.append((nx, ny))
    return graph[n - 1][m - 1]

print(BFS(0,0))