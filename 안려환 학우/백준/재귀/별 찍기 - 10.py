import sys

n = int(sys.stdin.readline())
star_list = [['*'] * n for _ in range(n)] # 2차원 배열을 초기화할 땐 리스트 컴프리헨션 꼭
# 애초에 별로 다 채운다.
mul = n
count = 0

while mul != 1:
    mul /= 3
    count += 1  # 입력받은 값이 3의 몇 제곱인가 확인해준다.

for j in range(count):
    blank = [i for i in range(n) if (i//3 ** j) % 3 == 1]  # 빈칸으로 채울 행열 인덱스라고 한다.
    # blank 안에는 9,10,11,12,13,14,15,16,17 들어가있음 
    # 그니까 빈 공간이 들어갈 줄에 대해서 지정해주는 것이다.
    
    for i in blank:
        for j in blank: # 이 이중 포문이 들어간 이유는 2차원 배열의 값들을
            star_list[i][j] = ' ' #띄워야할 곳들에 넣어주기 위함이다.

print('\n'.join([''.join([str(i) for i in row])for row in star_list]))





# join 은 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꿔 변환
# 그래서 '\n'라는 구분자를 이용해서 각 줄에 대한 개행을 해주고
# 행 안에 있는 별들은 개행없이 붙여서 출력하기 위함이다. 
# 저 row에는 *과 공백이 들어있으며 그 *과 공백에 대한 i를 문자형대로 띄어쓰기 없이
# 조인연산을 해준 것이다.

# 이 풀이가 제가 두 번째로 생각했던 아이디어로 푸는 방법입니다....
# 여기서 2차 배열을 이용하고 마지막 print 문은 정말 인상이 깊습니다....

# 처음엔 9개짜리 별만들기는 성공하였는데 그걸 이제 다른 함수에
# 집어 넣어서 사용하는 방법을 했는데 
# 함수호출 이후 개행문자를 제거하는 방법을 못찾아서 실패하였읍니다... 
# 또 입력받은 만큼의 수의 제곱만큼 별을 만들어서
# 빈칸이 만들어지는 부분과 개행문자가 나와야할 곳을 별과 바꿔서 해보려 했는데
# 규칙찾는게 매우 어려워서 실패하였읍니다... 그리고 개행으로 바꿔 출력하게
# 하는 방법을 못찾아서 실패하였읍니다....
# *** * * *** 이렇게 리스트를 만들어서 하려했는데 이게 개행을 억지로 만들어주는데 어려움
# 이 있어서 못하였읍니다.... 그 개행 넣을 때 안넣을 때 규칙 넣기가 매우 어렵워
# 이 또한 실패하였읍니다....
# 결국 검색을 해보았읍니다....

# def star(i):
#     global star_list
#     blank = [i for i in range(n) if (i // 3 ** i) % 3 == 1]
#     for i in blank:
#         for j in blank:
#             star_list[i][j] = ' '
#     print(blank)

# n = int(sys.stdin.readline())
# mul = n
# count = 0

# while mul != 1:
#     mul /= 3
#     count += 1

# star_list = [['*'] * n for _ in range(n)]

# for i in range(count):
#     star(i)

# print('\n'.join([''.join([str(i) for i in row])for row in star_list]))