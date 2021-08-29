import sys
from typing import Counter

insert_nums = []
for i in range(0,3):
    num = int(sys.stdin.readline())
    insert_nums.append(num)
    if len(insert_nums) == 1:
        multiple = insert_nums[0]
for i in range(1,3):
    multiple = multiple * insert_nums[i]

total = len(str(multiple))

print(multiple)
print(total)