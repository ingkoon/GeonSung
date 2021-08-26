import sys

N = int(sys.stdin.readline())
save_list = []
# I used list for reverse that number list

if N > 0 and N <= 100000 :
    for i in range(1, N + 1):
        save_list.append(i)
    save_list.reverse()
    for i in range(len(save_list)):
        print(save_list[i])
else:
    print("Out of range")