total = []
total_sum = 0
with open('안려환 학우\\코드잇\\프로그래밍 기초 in Python\\data\\chicken.txt','rt', encoding='UTF8') as f:
    for i in f:
        total.append(i.strip().split())

for i in range(len(total)):
    total_sum += int(total[i][1])
        
print(total_sum / 31)