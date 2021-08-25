test_num = int(input())
save_list = []
# to save a and b values

for i in range(0,test_num):
    a, b = map(int,input().split(" "))
    save_list.append(a)
    save_list.append(b)
#collect all values in save_list

j = 0
while j < len(save_list):
    print(save_list[j] + save_list[j + 1])
    j += 2
#calc this summary