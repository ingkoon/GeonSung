import random

comp_list = []
with open('안려환 학우\\코드잇\\프로그래밍 기초 in Python\\data\\vocabulary.txt','rt', encoding='UTF8') as d:
    for i in d:
        comp_list.append(i.strip().split(': '))


while True:
    rand = random.randint(0,len(comp_list) - 1) # 그냥 for 문써서 순서대로 할 수도 있었으나 랜덤으로 물어보는게 
    check = input(f"{comp_list[rand][1]}: ") # 단어 암기에 더 도움이 될 것이기에 이렇게 했읍니다.
    if check == comp_list[rand][0]:
        print("맞았습니다!")
    elif check == 'q': # 종료가 q이고 이걸 누르기 전까진 계속 합니다.
        break
    else:
        print(f"아쉽습니다. 정답은 {comp_list[rand][0]}입니다.")