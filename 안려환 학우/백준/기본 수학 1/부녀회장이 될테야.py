import sys

T = int(sys.stdin.readline())


for _ in range(T): # 이코테서 보고 배웠읍니다... _ 변수 신경안쓰고 반복문 쓰기
    floor_k = int(sys.stdin.readline())
    ho_n = int(sys.stdin.readline())
#변수 이름 설정의 중요성을 알게 되었읍니다...
#2차 배열을 이용해야하나 싶었읍니다... 일단 뭐라도 하나 해놓기 위해서 

    floor_0 = [i for i in range(1,ho_n + 1)] #0층은 1부터 n이다.

    for _ in range(floor_k): #입력받은 층수만큼 변수 신경쓰지 않고 반복
        for j in range(1,ho_n): #인덱스 0은 무조건 1이기에 1번 인덱스부터 더해주기 위함이다.
            floor_0[j] += floor_0[j - 1] # 모든 인원수가 가장 좌측에 있는 1부터 더해지기 시작.
    print(floor_0[-1])  #그니까 이건 0으로부터 1을 구하는 것부터 시작하는 것이다.
