import sys

def dfs(graph, v, visited): # dfs의 재귀형식을 이용
    visited[v] = True
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == False: # 이게 중요하다. 1로 연결이 되어있고 방문한 적이 없으면
            dfs(graph, i, visited) # 바이러스가 감염이 된다.

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
visited = [False] * n

graph = [[0] * n for _ in range(n)] # 인접 행렬을 이용해 준다.
# 각 노드별로 연결되었는지 안되었는지 확인하기 위한 인접행렬이다.
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1 # 1 과 2의 연결을 체크하기 위해 행렬이라 두 곳을 1로 해주어야 한다.
    graph[b - 1][a - 1] = 1 # 빼는 이유는 인덱스로 들어가야하기 때문이다. 
    # 문제에서는 1부터 시작하기 때문.


dfs(graph, 0, visited)
count = 0

for i in range(n): # 이제 바이러스 걸린 노드의 수를 세어준다.
    if visited[i] == True:
        count += 1

count -= 1 # 아 1번 컴퓨터로 인해 바이러스에 걸리는 녀석을 빼주어야 한다.
print(count)