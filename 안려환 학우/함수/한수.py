import sys


def hansu(a):
    han = 0
    hot = 0
    if N > 1000 or N < 1:  #N의 조건
        print("You typed wrong number")
    else:
        #인터넷을 봤는데 한자리와 두 자리 수는 모두 한수로 인정이 된다고 한다.
        for i in range(1, N+1):
            if i < 100:
                han += 1
            else:
                hot = list(map(int,str(i))) #인터넷에서 보고 왔읍니다....숫자를 자릿수대로 분리
                if hot[0] - hot[1] == hot[1] - hot[2]:   #각 자리의 차이가 등차인지 확인
                    han += 1
    return han


N = int(sys.stdin.readline())
print(hansu(N))  #함수호출해준다.