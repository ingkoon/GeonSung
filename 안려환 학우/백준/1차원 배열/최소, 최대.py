import sys 

N = int(sys.stdin.readline())
org_list = []
bigger_num = 0
smaller = 0
org_list += map(int,sys.stdin.readline().split(" "))

if len(org_list) != N:
    print(f"You have to enter {N} numbers")
else:
    org_list.sort() #미안하다.
    print(f"{org_list[0]} {org_list[N-1]}")
