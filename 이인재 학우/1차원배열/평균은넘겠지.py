import sys

cnt = int(sys.stdin.readline())
arr = []

for i in range(cnt):
    num = 0
    n = list(map(int, input().split(" ")))
    k = n.pop(0)
    avg = sum(n)/k
    for r in range(len(n)):
        if n[r] > avg:
            num += 1
    arr.append(float(num/k) * 100)


for j in range(len(arr)):
    print("%0.3f" %arr[j], end = "%\n")