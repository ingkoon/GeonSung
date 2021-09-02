import sys

cnt = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

print("%d %d" %(min(num), max(num)))

