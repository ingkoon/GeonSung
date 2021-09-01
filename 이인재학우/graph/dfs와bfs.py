import sys

n ,m ,v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(m+1)]

for i in range(1, m+1):
    graph[i] = list(map(int, sys.stdin.readline().split()))

print(graph)

visited = [False for i in range(n+1)]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')

    for i in graph[v]:
        if not visited[i]:
            print('next is', i)
            dfs(graph, i, visited)

dfs(graph, v, visited)
