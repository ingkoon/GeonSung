# import sys
# sys.setrecursionlimit(10 ** 9)
# # # 아 이제 이해를 뛰어넘어서..... 끌려다니고있읍니다....

# n = int(sys.stdin.readline())
# tree = [[] for _ in range(n + 1)]
# parent = [0 for _ in range(n + 1)]

# for _ in range(n - 1):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     tree[a].append(b)
#     tree[b].append(a)

# def dfs(tree, v, parent):
#     for i in tree[v]:
#         parent[i] = v
#         dfs(tree, v, parent)

# dfs(tree, 1, parent)

# for i in range(2, n + 1):
#     print(parent[i]) 

import sys 


n = int(sys.stdin.readline()) 
tree = [[] for _ in range(n+1)] 

for i in range(n - 1): 
    a, b = list(map(int, sys.stdin.readline().rstrip().split())) 
    tree[a].append(b) # 서로 연결해주기 
    tree[b].append(a) 
    
que = [1] # 1부터 시작이므로 시작 전에 큐에 1을 넣어준다. 
visit = [False for i in range(n+1)] # 방문된 곳인지 확인하기 위함! 
result = {} # result[4] 는 4번 노드의 부모가 담긴다. 근데 이게 왜 딕셔너리로 해야하는지....
while que: 
    now = que.pop(0) # 현재 가르키는 노드 처음엔 1이 온다. 
    for i in tree[now]: # tree[1] 에 있는 요소를 꺼낸다. tree[1]에는 4와 6 
        if visit[i] == False: # 방문한 적이 없다면, 
            result[i] = now # 4번 노드에 대한 출력값으로 부모인 now=1 삽입 
            visit[i] = True # 방문했으므로 1으로 바꿔준다. 
            que.append(i) # 큐에 추가해 다음 탐색을 이어가도록 한다. 

for i in range(2, n+1): # 둘째줄부터 따져야 한다.
     print(result[i])

