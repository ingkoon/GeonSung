import sys
save_list = []
big_list = []
big_num = 0
big_index = 0
for i in range(0,9):
    a = int(sys.stdin.readline())
    if i == 0:
        save_list.append(a)
        big_list.append(a)
    else:
        save_list.append(a)
        big_list.append(a)
        big_list.sort() #응 포기 안해~
        big_num = big_list[-1]
        for j in range(len(save_list)):
            if save_list[j] == big_num:
                big_index = j
big_index += 1


print(big_num)
print(big_index)