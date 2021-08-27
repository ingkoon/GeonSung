import sys

N = int(sys.stdin.readline())
if  N >= 1 and N <= 100000:
    for i in range(1,N + 1):
        print(i) 
else:
    print("Out of range")