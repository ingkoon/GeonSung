import sys

n, m, k = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

first = data[-1]
second = data[-2]

count = int(m/(k+1)) * k
count += m % (k + 1)

result = 0

result += (count) * first

result += (m - count) * second

print(result)