import sys

insert_nums = []
for i in range(0,3):   #입력받기 위해
    num = int(sys.stdin.readline())
    insert_nums.append(num)  #받은 값들을 리스트에 모아준다.
    if len(insert_nums) == 1:   #리스트 안에 값이 하나면 곱하기가 안되니까
        multiple = insert_nums[0]


for i in range(1,3):  #나머지 숫자들 곱셈연산해주기 위해서
    multiple = multiple * insert_nums[i]


count_list = (str(multiple)) #곱한 수 안에 각 숫자들을 카운트하기 위해 문자열로 변환
for i in range(10):
    count_num = count_list.count(str(i))  #도저히 안풀려서 인터넷 검색함. count라는 것을 알게 됨
    print(count_num)  #count는 이렇게 쓰는데 str(i)해서 이 문자가 있나 세서 총몇인지 알려줌