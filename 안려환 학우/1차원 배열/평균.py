import sys

insert_list = []
sum = 0
N = int(sys.stdin.readline()) 
insert_list += map(float,sys.stdin.readline().split(" "))

if len(insert_list) != N:
    print(f"You have to ender {N} numbers!")
else:
    insert_list.sort()
    M = insert_list[-1]
    for i in range(N):
        insert_list[i] = insert_list[i] / M * 100
for i in range(N):
    sum += insert_list[i]
final = sum / N
print(final)