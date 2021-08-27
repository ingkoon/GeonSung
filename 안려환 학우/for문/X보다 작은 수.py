import sys

N, X = map(int,sys.stdin.readline().split(" "))
save_list = []
other_list = []

save_list += map(int,sys.stdin.readline().split(" "))

for i in range(len(save_list)):
    if save_list[i] < X:
        other_list.append(save_list[i])

if len(other_list) == 0:
    print("You typed wrong numbers please include bigger than X more than 0")
else:
    result = ''
    for i in range(len(other_list)):
        result = result + str(other_list[i]) + " "
    print(result)
    #To print list in one line