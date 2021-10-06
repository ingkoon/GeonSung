import random

def generate_numbers(n):
    gen = []
    for _ in range(n):
        gen.append(random.randint(1,45))
    check = set(gen)
    if len(gen) != len(check):
        return generate_numbers(n)
    else:
        return gen


def draw_winning_numbers():
    draw = generate_numbers(6)
    draw.sort()
    n = generate_numbers(1)
    # check_bool = n[0] in draw    # case 1.
    # if check_bool == True:
    #     return draw_winning_numbers()
    # else:
    #     draw.append(n[0])
    #     return draw
    draw += n
    check = set(draw)
    if len(draw) != len(check):
        return draw_winning_numbers()
    else:
        return draw

goal = draw_winning_numbers()
usr_auto = generate_numbers(6)

def count_matching_numbers(usr, goal):
    count = 0
    bonus = False
    check = []      #이게 진짜 랜덤의 숫자를 가지고 보너스숫자까지 염두해 푸는 방식
    for i in range(len(usr)):
        if goal[i] in usr:
            count += 1
    if goal[6] in usr:
        bonus = True
    check.append(count)
    check.append(bonus)
    return check

    # for i in range(len(usr)):  # 이건 아무짝에 의미없는 매칭넘버
    #     if usr[i] in goal:     # 이 답을 코드잇은 원한다.
    #         count += 1
    # return count

def check(a):
    if a[0] == 6:
        print('1000000000')
    elif a[0] == 5 and a[1] == True:
        print('50000000')
    elif a[0] == 5 and a[1] == False:
        print('1000000')
    elif a[0] == 4:
        print('50000')
    elif a[0] == 3:
        print('5000') 
    else:
        print('꽝!')

check(count_matching_numbers(usr_auto,goal))



# def count_matching_numbers(usr, goal):  # 코드잇이 원하는 코드
#     count = 0
#     bonus = False
#     check = []      #이게 진짜 랜덤의 숫자를 가지고 보너스숫자까지 염두해 푸는 방식
#     for i in range(len(usr)):
#         if goal[i] in usr:
#             count += 1
#     if goal[6] in usr:
#         bonus = True
#     check.append(count)
#     check.append(bonus)
#     return check

#     # for i in range(len(usr)):  # 이건 아무짝에 의미없는 매칭넘버
#     #     if usr[i] in goal:     # 이 답을 코드잇은 원한다.
#     #         count += 1
#     # return count

# def check(a):
#     if a[0] == 6:
#         print('1000000000')
#     elif a[0] == 5 and a[1] == True:
#         print('50000000')
#     elif a[0] == 5 and a[1] == False:
#         print('1000000')
#     elif a[0] == 4:
#         print('50000')
#     elif a[0] == 3:
#         print('5000') 
#     else:
#         print('꽝!')

# # 테스트
# check(count_matching_numbers([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# check(count_matching_numbers([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))