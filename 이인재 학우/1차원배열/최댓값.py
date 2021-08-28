import sys

arr = [0 for i in range(9)]

for i in range(9):
    arr[i] = int(sys.stdin.readline())

print(max(arr))
print(arr.index(max(arr))+1)
