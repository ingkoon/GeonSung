import sys

a = 1
b = 1
sum = []
while a != 0 and b != 0:
    a, b = map(int,sys.stdin.readline().split(" "))
    if a == 0 and b == 0:
        break
    else:
        sum.append(a + b)


for i in range(len(sum)):
    print(f"{sum[i]}")