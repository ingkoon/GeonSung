import sys

while 1:
    try:
        a, b = map(int,sys.stdin.readline().split(" "))
        if a < 0 or b > 10:
         break
        else:
          print(a + b)
    except:
        break
#문제 자체를 이해 못함
#트라이엑셉트 왜 하는지 왜 필요한지
#그냥 테스트 차원에서 하는건지 모르겠음