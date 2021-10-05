import random

comp_list = []
key_list = []
value_list = []
with open('안려환 학우\\코드잇\\프로그래밍 기초 in Python\\data\\vocabulary.txt','rt', encoding='UTF8') as d:
    for i in d:
        comp_list.append(i.strip().split(': '))

dic = {}
for i in range(len(comp_list)):
    dic[comp_list[i][0]] = comp_list[i][1]


while True:
    rand = random.randint(0,len(dic) - 1) # 무작위로 물어보기 위함입니다.
    key = list(dic.keys()) # 사전의 키값들을 가져와서 그들과 비교해줍니다. 사전은 인덱스값이 없기에.
    check = input(f"{key[rand]}: ") 
    if check == dic[key[rand]]:
        print("맞았습니다!")
    elif check == 'q': # 종료가 q이고 이걸 누르기 전까진 계속 합니다.
        break
    else:
        print(f"아쉽습니다. 정답은 {dic[key[rand]]}입니다.")