import sys

n = int(sys.stdin.readline())
fivo = [i for i in range(n + 1)]
i = 0
for i in range(n+1):
    if i >= 2:
        fivo[i] = fivo[i - 2] + fivo[i - 1]
print(fivo[-1])

# 얘까지 좋습니다....