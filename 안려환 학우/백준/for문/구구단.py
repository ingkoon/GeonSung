a= int(input())
if a >= 1 and a <= 9:
    for i in range(1,10):
        print(f"{a} * {i} = {a * i}")
else:
    print("That's nono")