total = []
total_sum = 0
with open('data\chicken.txt','r') as f:
    for i in f:
        total.append(i.strip().split())

for i in range(len(total)):
    total_sum += int(total[i][1])
        
print(total_sum / 31)