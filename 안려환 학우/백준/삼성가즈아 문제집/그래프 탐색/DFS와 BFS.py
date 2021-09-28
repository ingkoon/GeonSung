import sys

# n, m, v = map(int,sys.stdin.readline().split())
# visited = [False] * n
# graph = [[0] * n for _ in range(n)]

# visited = [False] * n

# for _ in range(m):
#     a, b = map(int,sys.stdin.readline().split())
#     graph[a - 1][b - 1] = 1
#     graph[b - 1][a - 1] = 1

# def DFS(v):
#     print(v, end = ' ')
#     visited[v] = True

#     for i in range(n):
#         if graph[v][i] == 1 and visited[i] == False:
#             DFS(i)

# DFS(v) 이전꺼 이용해서 하려했는데 실패했읍니다...

def dfs(v):
    print(v, end=' ')
    visit[v] = 1  # true false 를 1 0 으로 나눠서 함.
    for i in range(1, n + 1): # 노드가 1부터 있으니 그렇게 설정을 해준다.
        if visit[i] == 0 and s[v][i] == 1:  # 보면 방문한 적이 없고 간선있는 곳을 가고
            dfs(i) # 재호출 재귀를 통해서 푼다.

def bfs(v):
    queue = [v] # BFS는 큐를 이용하니 디큐를 써준다.
    visit[v] = 0
    while(queue):
        v = queue[0] # 시작점을 큐의 처음부로
        print(v, end=' ')
        del queue[0] # 이걸 print(queue.popleft(), end = ' ')는 안되는 거였읍니다...
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1: # 방문한적있고 간선있는건 빼버립니다.
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)