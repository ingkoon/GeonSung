# DFS(깊이우선탐색) 기본

# 그래프의 깊은 부분을 우선적 탐색 수행

# 노드, 간선, 정점 이렇게 구성되어있음

def dfs(graph, v, visited):
    # 방문 노드는 True로 수정
    visited[v] = True
    # 출력
    print(v, end=' ')
    # 노드에 연결된 간선을 가져와 dfs함수를 통해 재귀를 통해 반복 수행
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [], 
    [2, 3, 8], 
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7]
    ]

visited = [False] * 9 
dfs(graph, 1, visited)