import sys

N = int(sys.stdin.readline())

if N >= 1 and N <= 100:
    for i in range(1,N + 1):
        blank = N - i
        print(" " * blank+"*" * i)
else:
    print("Out of Range")