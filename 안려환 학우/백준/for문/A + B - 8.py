import sys
sum_list = []
a_list = []
b_list = []
#To save inputed values

T = int(sys.stdin.readline())
for i in range(0, T):
    a, b = map(int,sys.stdin.readline().split(" "))
    sum_list.append(a+b)
    a_list.append(a)
    b_list.append(b)
for i in range(0, T):
    print(f"Case #{i + 1}: {a_list[i]} + {b_list[i]} = {sum_list[i]}")