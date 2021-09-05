#1 6 12 18 24 6의 배수로 증가된다. 
#str_n = str(N) 썩은 생각 자릿수로는 안된다.
import sys

N = int(sys.stdin.readline())
count = 1 #몇 번 지나는지
check_N = 1 #벌집의 칸의 개수


while N > check_N:
    check_N += 6 * count #6차이씩 커지니까 그만큼씩 계속 더해줘야함.
    count += 1
print(count)
