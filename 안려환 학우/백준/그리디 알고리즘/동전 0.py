import sys

# 책에서 보기에 가장 대표적인 그리디 문제라고 합니다...
# 그리디 알고리즘은 일단 가장 좋은 것만 고르는 것
# 가장 큰 수부터 먼저 빼내고 이후의 상황은 신경쓰지 않는다고 합니다.

coin, money = map(int,sys.stdin.readline().split(" "))
coin_list = [0 for _ in range(coin)] # append를 최대한 적게 쓰기 위함입니다...
count = 0

for i in range(coin):
    co = int(sys.stdin.readline())
    coin_list[i] = co

# 책에서 본 내용을 가지고 적어보겠읍니다...

coin_list.sort() # 혹시 수를 이상하게 대입해줄까봐 정렬을 한 번 해주었읍니다.
coin_list.reverse() # 그리디를 위해서 역으로 정렬을 해주었읍니다.

for i in coin_list:
    count += money // i # 이해가 쉽읍니다... 큰 수부터 넣었기에 그리디 알고리즘으로
    money %= i # 해결을 하였읍니다... 이건 나머지를 가지고 또 나눠주어야 하기 때문입니다.

print(count)