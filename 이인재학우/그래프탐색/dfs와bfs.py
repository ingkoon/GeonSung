import sys
from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n ,m ,v = map(int, sys.stdin.readline().split())

# 그래프를 2차원 리스트 형태로 지정
graph = [[] for i in range(n+1)]

# for 문을 통해 시작 지점과 연결된 목적지점을 리스트에 추가
for i in range(m):
    s, d = map(int, sys.stdin.readline().split())
    graph[s].append(d)
    graph[d].append(s)

for i in range(m):
    graph[i].sort()

# 방문한 정점에 대해 True로 바꿀 수 있도록 지정
visited = [False for i in range(n+1)]

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:        
            dfs(graph, i, visited)


# bfs
def bfs(graph, v, visited):
    queue = deque([v])

    visited[v] = True

    while queue:
        val = queue.popleft()
        print(val, end = ' ')
        for i in graph[val]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)

visited = [False for i in range(n+1)]

print()

bfs(graph, v, visited)
