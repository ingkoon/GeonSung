import sys

n, m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline()))) # 이럼 기본 틀이 완성된다.
# deque는 popleft를 할 일이 없다면 굳이 쓰이지는 않는 것 같다.
# 더욱이 dfs는 재귀를 이용하지 큐를 이용하지 않기에 쓰지 않는다.

def DFS(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 기본 틀에서 밖으로 나가면 종료
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 음 왜 기본 틀을 1로 바꾸는지....
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True # 이렇게 트루 채워진 곳만 음료가 채워지기 떄문
    return False


# 이제 음료수를 채운다고 합니다...
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if DFS(i, j) == True:
            result += 1

print(result)


