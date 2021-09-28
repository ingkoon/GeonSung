import sys
sys.setrecursionlimit(10000) # 이게 재귀에 제한을 걸어두는 것이다. 이게 없으면 런타임 에러가 걸린다.
# 그럼 dfs 를 사용할 때는 이렇게 걸어주는게 좋을 듯

n, m = map(int, sys.stdin.readline().split())
s = [[0] * (n + 1) for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
count = 0


def dfs(v):
    visit[v] = True
    for i in range(1, n + 1):
        if s[v][i] == 1 and visit[i] == False: # 연결된 상태에 방문안했으면
            dfs(i)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = 1 # 인접 행렬에 연결을 표시하는 것.
    s[b][a] = 1
for i in range(1, n + 1):
    if visit[i] == False: # 방문한적이 없는 노드는 연결이 안된 것이다.
        dfs(i)
        count += 1 # 그러니 연결된 요소가 하나 추가되는 것이다.


print(count)