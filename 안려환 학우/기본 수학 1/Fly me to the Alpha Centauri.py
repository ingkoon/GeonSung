import sys

T = int(sys.stdin.readline())
final = []
count = 0
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split(" "))
    while a != b:
        if a + 2 == (b - 1):
            a += 1
            count += 2
        else:
            if a == b - 1:
                a += 1
                count += 1
            else:
                a += 2
                count += 1
    print(count)

