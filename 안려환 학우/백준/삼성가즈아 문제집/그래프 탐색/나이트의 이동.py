import sys
from collections import deque

# input_str = str(sys.stdin.readline())


# # 체스 판을 만들어 주었읍니다.
# # 각 칸의 규칙 찾아넣으려니 매우 많은 시간이 들었읍니다...
# # 상하좌우처럼 이동하는 방향 경우 모아준다.

# directions = [[1,2], [-1,2], [1,-2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]] # 방향들을 전부 모아줍니다.
# final_w = 0
# final_h = 0
# count = 0

# def BFS(graph, start, visited):
#     que = deque()
#     visited[start] = True
#     while que:
#         a = que.popleft()
#         print(a, end = ' ')
#         for i in graph[a]:
#             if not visited[i]:
#                 que.append(i)
#                 visited[i] = True

# for i in directions:
#     final_w = w + i[1] # 각 리스트의 세로 움직임
#     final_h = h + i[0] # 각 리스트의 가로 움직임
#     if final_w >= 1 and final_w <= 8 and final_h >= 1 and final_h <= 8: # 체스판 밖으로 나가는 경우
#         count += 1

# print(count)



# # 나이트 이동 경우
# dx = [-1, -2, -2, -1, 1, 2, 2, 1]
# dy = [2, 1, -1, -2, -2, -1, 1, 2]


# def bfs(x_1, y_1, tx, ty):
#     queue = deque()
#     queue.append([x_1, y_1])
#     graph[x_1][y_1] = 1

#     while queue:
#         now_x, now_y = queue.popleft()
#         if now_y == ty and now_x == tx:
#             print(graph[tx][ty]-1)
#             return
#         for i in range(8):
#             nx = now_x + dx[i]
#             ny = now_y + dy[i]
#             if 0 <= ny < n and 0 <= nx < n and graph[nx][ny] == 0:
#                 graph[nx][ny] = graph[now_x][now_y] + 1
#                 queue.append([nx, ny])


# t = int(sys.stdin.readline())


# for i in range(t):
#     # 체스판 한 변의 길이 n
#     n = int(sys.stdin.readline().split())
#     # 현재 나이트의 위치
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     # 이동하려고 하는 칸
#     target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

#     graph = [[0] * n for _ in range(n)]

#     bfs(x, y, target_x, target_y)



dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy]) # 시작점은 있어야 한다.
    s[sx][sy] = 1
    while q:
        a, b = q.popleft() # 기존 BFS형태 빼주면서 그 아래 이동가능한 노드들을 전부 append 해주기 위함이다.
        if a == ax and b == ay:  # 목표에 도달했다면
            print(s[ax][ay] -1) # 처음 시작점 1을 빼준다.
            return
        for i in range(8):
            x = a + dx[i] # 아까 꺼낸 값을 가져와서 이동가능한 경우로 계산해 위치를 정해준다.
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y]) # 칸 안에 있으면 이 경우를 queue에 넣어준다.
                s[x][y] = s[a][b] + 1 # 이동횟수를 더해준다.


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().rstrip().split())
    ax, ay = map(int, sys.stdin.readline().rstrip().split()) # 매번 입력을 받기 위함이다.
    s = [[0] * n for _ in range(n)] # 계속 초기화를 해줘야 한다.
    bfs(sx, sy, ax, ay)