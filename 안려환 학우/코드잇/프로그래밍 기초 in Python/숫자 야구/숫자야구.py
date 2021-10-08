from random import randint
count = 1
game_count = 1
input_list = []

def generate_rand():
    rand_list = []
    for _ in range(3):
        rand_list.append(randint(0, 9))
    check = set(rand_list)
    if len(rand_list) == len(check):
        return rand_list
    else:
        return generate_rand()


def input_num(count):
    final_list = []
    if count < 4:
        a = int(input(f'{count}번째 숫자를 입력하세요: '))
        if len(input_list) == 0:
            if a < 10:
                input_list.append(a)
                count += 1
                return input_num(count)
            else:
                print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
                return input_num(count)
        else:
            check = a in input_list
            if a < 10:
                if check == True:
                    print('중복되는 숫자 입니다. 다시 입력하세요.')
                    return input_num(count)
                else:
                    input_list.append(a)
                    count += 1
                    return input_num(count)
            else:
                print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
                return input_num(count)
    else:
        for i in range(3):
            final_list.append(input_list[i]) # 요소들을 직접 넣어줍니다.
        input_list.clear() # 파이썬이 배열을 =처리하게 되면 주소를 가리키게되어서 문제가 발생합니다.
        return final_list



def check(num_list,in_list):
    s_count = 0
    b_count = 0
    for i in range(3):
        if num_list[i] == in_list[i]:
            s_count += 1
    for i in range(3):
        for j in range(3):
            if num_list[j] == in_list[i]:
                b_count += 1
    total = str(s_count) + 'S ' + str(b_count) + 'B'
    print(total)
    return s_count


num_list = generate_rand()
print('0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n')


def game(game_count):
    print('숫자 3개를 하나씩 차례대로 입력하세요.')
    a = check(num_list,input_num(count))
    if a == 3:
        print(f'\n축하합니다. {game_count}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.')
    else:
        game_count += 1
        game(game_count)


game(game_count)

