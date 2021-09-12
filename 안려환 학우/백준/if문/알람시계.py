a, b = map(int,input().split(" "))
if b < 45:
    b = b + 60 - 45
    if a == 0:
        a = 23
    else:
        a -= 1
    print(f"{a} {b}")
else:
    print(f"{a} {b - 45}")
