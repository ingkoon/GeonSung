import sys

h, s = map(int, sys.stdin.readline.split())

if h <= 23 and h>0:
    if s >=45:
        s = s -45
    else:
        h -= 1 
        s = 60 - (45 - s)
else:
    if s>=45:
        s = s-45
    else:
        h = 23
        s = 60 - (45 - s )

print("%d %d" %(h,s))