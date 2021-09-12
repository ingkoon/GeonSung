#8393
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
#range(start, stop-1, distance)
#so I have to stop -1 +1 
#Then I can get just stop
print(sum)