import sys

a = 0
cycle = 0
N = int(sys.stdin.readline())

if N < 10:
    cycle += 1
    a = N * 11
    while a != N:
        if a < 10:
            cycle += 1
            a = a * 11
        else:
            cycle += 1
            b = a // 10 + a % 10
            a = a % 10 * 10 + b % 10

elif N == 0:
    print("1")

else:
    cycle += 1
    b = N // 10 + N % 10
    a = N % 10 * 10 + b % 10  #이거 없으면 시간이 매우 오래 걸린다.
    while a != N:
        if a < 10:
            cycle += 1
            a = a * 11
        else:
            cycle += 1
            b = a // 10 + a % 10
            a = a % 10 * 10 + b % 10

print(cycle)

#먼저 제일 첫 경우를 걸러준 후 
#이후 과정에 while 넣어줬다.
#0은 따로 뺐다.