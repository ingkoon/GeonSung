#2557
# print("Hello World!")

#10718
# print("강한친구 대한육군\n강한친구 대한육군")

# 10171
# print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")
#I used \n to follow PEP3 as know as Python style guide
# I remember Python has to finish in one line

# 10172
# print("|\_/|\n|q p|   /}\n( 0 )\"\"\"\ \n|\"^\"`    |\n||_/=\\\__|")
# #I missed one slash and I used \ to print""

#1000 - quiz of map **
#I forgot how to use map method so I saw hint 
# a, b = map(int, input().split(" "))
# print(a + b)

#1001 - quiz of map
# a, b = map(int, input().split(" "))
# print(a - b)

#10998 - quiz of map
# a, b = map(int, input().split(" "))
# print(a * b)

#1008
# a, b = map(int, input().split(" "))
# under_ten = a / b
# print(round(under_ten, 9))
# # I saw about special round of Python
# # If value is near to less value then Python return less
# # round(0.5) : 0 # 0.5의 반올림이 1이 아니라 0 ??? 
# # round(1.5) : 2 round(4.5) : 4 보면 4와 5 사이에 0.5란 양쪽
# # 4와 5의 딱 중간에 있는 수라서 짝수인 2를 출력해버린다.

#10869
# a, b = map(int, input().split(" "))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
#I couldn't use \n because these are not 문자열

#10430
# a, b, c = map(int, input().split(" "))
# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c) * (b % c)) % c)

#2588
# a = int(input())
# b = int(input())
# thousand = b // 100
# ten = b % 100 // 10
# one = b % 100 % 10
# list_1 = [one,ten,thousand]
# for i in range(3):
#     print(list_1[i] * a)
# print(a * b)