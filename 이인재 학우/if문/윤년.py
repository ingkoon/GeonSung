import sys

a = int(sys.stdin.readline())

n1 = 4
n2 = 100
n3 = 400

if(a%n1 == 0 and (a%n3 ==0 or a%n2 !=0)):
    print("1")
else:
    print("0")
