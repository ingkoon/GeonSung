import sys
from collections import deque
n ,m ,v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(m+1)]

for i in range(m):
    s, d = map(int, sys.stdin.readline().split())
    graph[s] = d
    graph[d] = s

print(graph)

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
