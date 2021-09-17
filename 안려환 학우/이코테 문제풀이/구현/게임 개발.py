import sys

# 처음 맵 크기를 설정해준다.
# 이후 캐릭터의 위치와 바라보는 방향이 주어진다.
# 맵은 1은 바다 0은 육지이다.
# 1인 바다와 맵 밖의 지형으로는 갈 수 없다.
# 0으로만 갈 수 있는 것이다.
# 출력은 이동을 마친 캐릭터가 방문한 칸의 수를 나타내는 것이다.


# 문제 있는 그대로
# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 
# 차례대로 갈 곳을 구한다.
# 캐릭터의 바로 왼쪽 방향에 아직 못가본 칸이 존재한다면 왼쪽 방향으로 회전만
# 1회 수행하고 1단계로 돌아간다.
# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는
# 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
# 단 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 돌아갈 수 없는 경우에는 움직임을 멈춘다.

# 입력 
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 출력
# 3
# 북: 0 동: 1 남: 2 서: 3

n, m = map(int,sys.stdin.readline().rstrip().split())
x, y, direction = map(int,sys.stdin.readline().rstrip().split())
array = [[0] * m for _ in range(n)] # 이차원 배열은 무조건 리스트 컴프리헨션을 이용하자.
for i in range(n):
    array[i] = sys.stdin.readline().rstrip().split()
# 입력값 설정 완료


# # 방향을 지정하는 리스트
# dir_list = [[-1,0], [0,1], [1,0], [0,-1]] # 이렇게 되는 이유는 계속 왼쪽부터 시작으로 방향을 확인하기 때문이다.
#           #[왼,아래,오른,위]
d = [[0] * m for _ in range(n)]
d[x][y] = 1
# sum_h = 0
# sum_w = 0
# count = 0
# # 가봤는지 확인하기 위해 모두 0인 2차 배열을 선언해준다.
# # 책에서처럼 함수를 하나 만들어 보자
# def move_(map_list,dir_list,a_h,a_w,count):
#     moving = 0
#     for i in range(w):
#             sum_h = a_h + dir_list[i][0]
#             sum_w = a_w + dir_list[i][1]
#             if sum_w <= 0 and sum_h <= 0 and sum_w >= w and sum_h >= h :
#                 continue
#             else:
#                 if map_list[sum_h][sum_w] == 0  and check_map[sum_h][sum_w] == 0:
#                     count += 1
#                     a_w = sum_w
#                     a_h = sum_h
#                     check_map[a_h][a_w] = 1
#                     moving += 1
#                 elif map_list[sum_h][sum_w] == 1  or check_map[sum_h][sum_w] == 1:
#                     continue
#     return count


# check_map[a_h][a_w] = 1 # 시작점 가본 곳으로 설정해 둔다.
# for _ in range(h):
#     move_(map_list,dir_list,a_h,a_w,count)

# print(count)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전에 대한 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 저염넹 안가본 곳 잇으면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break

        turn_time = 0

print(count)
# 책으로 풀어도 안풀립니다... 3시간 소요 후 시간 낭비