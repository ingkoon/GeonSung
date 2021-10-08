# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 예제 입력 1 
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 예제 출력 1 
# 2

import sys

# 정점과 간선의 개수를 입력받는다
n, m = map(int, sys.stdin.readline().split())

# {1:[], 2:[], 3:[] .... } 이런 딕셔너리 형식으로 구성이 된다
graph = {i:[] for i in range(1, n+1)}

# 방문한 정점에 대해서 True표시를 할 것이기 때문에 배열 지정
visited = [False for i in range(n + 1)]

# 각각의 정점에 대한 입력을 받아 딕셔너리에 추가
for _ in range(m):
    k, v = map(int, sys.stdin.readline().split())
    graph[k].append(v)


def dfs(visited, v):
    # 방문 되지 않은 정점일 경우 방문 체크
    if visited[v] == False:
        visited[v] = True
        print('visited', v)
        # 해당 정점에 연결된 다른 정점을 모두 조회 및 dfs 재귀 수행 
        for i in graph[v]:            
            if visited[i] == False:                
                print('next part is', i)
                dfs(visited, i)       
        # 참값 반환
        return True
    # 없을 경우 False 반환
    return False

result = 0

for i in range(1, n):
    if dfs(visited, i) == True:
        result += 1

print(result)