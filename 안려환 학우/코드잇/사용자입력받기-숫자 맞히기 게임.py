import random


# 코드를 작성하세요.
chance = 4
count = 1
num = random.randint(1,20)
def check(chance,count):
    if chance == 0:
        print(f"아쉽습니다. 정답은 {num}입니다.")
    else:
        check_num = int(input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
        if check_num > num:
            chance -= 1
            count += 1
            print("DOWN")
            check(chance,count)
        elif check_num < num:
            chance -= 1
            count += 1
            print("UP")
            check(chance,count)
        else:
            print(f"축하합니다. {count}번 만에 숫자를 맞히셨습니다.")

# 재귀로 풀어버리기
check(chance,count)