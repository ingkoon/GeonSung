# N*M 크기의 얼음 틀이 있다. 구멍이 뚤려 있는 부분은 0 칸막이가 존재하는 부분은 1로 표시된다.

# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.

# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

# 다음의 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

import sys

# 사용자 입력
n, m = map(int, sys.stdin.readline().split())

# 그래프 초기화
graph = []

# 그래프 내 값 할당
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# dfs함수 선언
def dfs(x, y):
    
    # 규격 외에 대한 에외처리
    if x <= -1 or x >= n or y <= -1 or y >= m:        
        return False
    
    # 값이 0 일 경우
    if graph[x][y] == 0:
        # 방문처리와 같이 1로 변경
        graph[x][y] = 1
        # 인접 노드를 dfs의 재귀를 통해 확인
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        # 참값 반환
        return True
    return False

# 결과를 위한 함수 선언
result = 0

# 전체 노드를 한번씩 훓을 수 있도록 2중 for문을 사용하여 처리
for i in range(n):
    for j in range(m):
        # True값이 반환된 부분이 발견될 경우
        if dfs(i, j) == True:
            # result에 1추가
            result += 1

# 결과 출력            
print(result)