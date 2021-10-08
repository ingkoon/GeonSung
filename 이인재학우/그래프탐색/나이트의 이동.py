# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
# 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.


# 결과적으로 모든 가능성을 탐색해야 하므로, bfs가 어울리지 않을까

import sys
from collections import deque

n = int(sys.stdin.readline())

# 모든 이동 경로에 대해 지정
nx = [1, 1, 2, 2, -1, -1, -2, -2]
ny = [2, -2, 1, -1, 2, -2, 1, -1]

# 너비우선 탐색
def bfs(x, y, dx, dy):
    # 큐 지정
    q = deque()

    # 입력되는 값 
    q.append([x, y])

    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == dx and y == dy:
            return visited[x][y]-1

        # 값을 하나씩 꺼내와 값 증감
        for i in range(len(nx)):
            tmpx = x + nx[i]
            tmpy = y + ny[i]

            # 단계를 거칠수록 값이 하나씩 늘어남
            if 0 <= tmpx < l and 0 <= tmpy < l:
                if visited[tmpx][tmpy] == 0:
                    q.append([tmpx, tmpy])
                    visited[tmpx][tmpy] = visited[x][y] + 1

for i in range(n):
    l = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    dx, dy = map(int, sys.stdin.readline().split())

    visited = [[0] * l for _ in range(l)]    
    if x == dx and y == dy:
        print(0)
        continue

    result = bfs(x, y, dx, dy)
    print(result)
    n -= 1
