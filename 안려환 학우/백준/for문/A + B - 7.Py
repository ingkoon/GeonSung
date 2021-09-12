import sys
sum_list = []
#To save inputed values

T = int(sys.stdin.readline())
for i in range(0, T):
    a, b = map(int,sys.stdin.readline().split(" "))
    sum_list.append(a+b)
for i in range(0, T):
    print(f"Case #{i + 1}: {sum_list[i]}")