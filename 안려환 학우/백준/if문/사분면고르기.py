a = int(input())
b = int(input())
if a > 0 and b > 0:
    print("1")
elif a > 0 and b < 0:
    print("4")
elif a < 0 and b > 0:
    print("2")
elif a < 0 and b < 0:
    print("3")
elif a == 0 and b < 0:
    print("on -y line")
else:
    print("I don't care")
# Oh I'm done It will be so tired