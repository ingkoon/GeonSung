import sys

n = int(sys.stdin.readline())
sum = 0

b_list = list(map(int,sys.stdin.readline().split()))

b_list.sort()

for i in range(n):
    for j in range(i + 1):
        sum += b_list[j]   #계속 누적해서 더해줘야한다.

        
print(sum)
