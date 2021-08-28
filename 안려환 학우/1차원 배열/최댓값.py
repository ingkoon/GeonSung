import sys
save_list = []

big_num = 0
big_index = 0
for i in range(0,9):
    a = int(sys.stdin.readline())
    if i == 0:
        save_list.append(a)
    else:
        save_list.append(a)
        if a > save_list[i]:
            
            big_num = a
            big_index = i
        else:
            big_num = save_list[i]
            
    

print(big_num)
print(big_index)