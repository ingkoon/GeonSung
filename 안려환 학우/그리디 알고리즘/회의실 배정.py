import sys

# 문제 이해하기
# 그러니까 이게 1 4면 1시에서 4시인거고 3 5 이면 3시부터 5시이다.
# 이 들을 조합해서 회의가 겹치지 않고 최대로 진행될 수 있는 
# 회의들의 조합을 알아내보자.

n = int(sys.stdin.readline())
mtng_list = [0 for _ in range(n)]
sum_list = [0 for _ in range(2)]

for i in range(n) :
    a, b = map(int,sys.stdin.readline().split(" "))
    mtng_list[i] = [a,b]

# 어떻게 해야하나 고민했읍니다... 원래는 리스트 하나 파서
# for i in range(i):
#   start_list[i] = mtnh_list[i][0]
#   end_list[i] = mtng_list[i][1]
# 이렇게 해서 각 시작 시간과 종료 시간들을 모아서 start 와 end를
# 가져와서 sort 해준 후 시작과 끝의 차이가 얼마 안나는 것끼리 모아서
# 각 이어붙이면서 count를 올려주고 해주려 했는데 그럼 시작과 끝이
# 다르게 정렬이 되어서 그것을 해결을 끝내 못해서 못풀게 되었읍니다....

