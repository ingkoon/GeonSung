import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().rstrip())) #훌륭쓰

#    total += nums[i]
#TypeError: unsupported operand type(s) for +=: 'int' and 'str'
#라는 에러가 발생하여 이걸 해결해주기 위해 이 list안에 들어갈 형태를 지정
#해줄 필요가 있었고 map을 이용해 list에 넣어줄 값들을 int라고 지정해줬다.
total = 0

if len(nums) != N:  #위의 숫자만큼 안하면 문제생기게 했다. rstrip안해주면
                    #마지막 개행문자때문에 한 줄 더 생겨서 rstrip으로 해결
    print("You entered wrong nums")
else:
    for i in range(len(nums)):
        total += nums[i]
print(total)