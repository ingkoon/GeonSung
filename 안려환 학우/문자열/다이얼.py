input_string = str(input()).lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dial = '33344455566677788889999999' #계산해보니 이대로 더해주면 되는 것
sum = 0
count = 0

if len(input_string) <= 15 and len(input_string) >= 2: #입력조건
    for i in range(len(input_string)): #입력받은 만큼 반복
        for j in range(len(alphabet)): #알파벡에서 확인해보려고
            if input_string[i] == alphabet[j]: #지금 이 if문으로 안들어옴
               if j >= 22:  #이때부턴 10이라 걍 9로 해두고 여기서 더해주려고
                   sum = sum + int(dial[j]) + 1  
               else:
                   sum += int(dial[j])
else:
    print("You entered wrong string")

print(sum)