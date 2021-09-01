# bfs 기본
# 너비 우선 탐색으로 가까운 노드부터 탐색하는 알고리즘

# 1. 탐색시작 노드를 큐에 삽입 후 방문처리 수행
# 2. 큐에서 노드를 껀 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번의 과정을 더이상 수행할 수 없을 때 까지 반복

# from collections import deque
# print("a")
# def bfs(graph, start, visited):
#     queue = deque([start])

#     # 방문 노드 체크
#     visited[start] = True

#     # 큐 내부에 아무 값도 없어질 때까지
#     while queue:
#         # 첫번째 값을 뺀다
#         v = queue.popleft()
#         print(v, end = ' ')
#         # for문을 사용하여 인접 노드의 값을 가져온다
#         for i in graph[v]:
#             # 방문되어 있지 않을 경우, 큐에 넣고 방문했음을 추가한다.
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [], 
#     [2, 3, 8], 
#     [1, 7], 
#     [1, 4, 5], 
#     [3, 5], 
#     [3, 4], 
#     [7], 
#     [2, 6, 8], 
#     [1, 7]
#     ]

# visited = [False] * 9 
# bfs(graph, 1, visited)

import os

currentPath = os.getcwd()

print(currentPath)

os.chdir(currentPath)

