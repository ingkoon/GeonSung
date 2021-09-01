
A,B =map(str,input().split(" "))
#readline() 손절합니다 ㅂㅂ
A = A[::-1]
B = B[::-1]  #문자열 뒤집기 [::-1]
a = int(A)
b = int(B)
if a > b:
    print(a)
else:
    print(b)