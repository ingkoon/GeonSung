# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 
# 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 
# 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 예를 들어서 2 4 5 4 6 으로 이루어진 배열이 있을 때 M 이 8이고 K가 3이라고
# 가정하면 특정한 인덱스가 3번까지 더해질 수 있으므로 이 법칙상 가장 큰 수는
# 6 6 6 5 6 6 6 5 인 46이 된다.
# 단 서로 다른 인덱스가 더해지는 경우엔 다른 수로 본다.
# 3 4 3 4 3  으로 이루어진 배열이 있을 때 M이 7이고 K가 2라고 가정한다.
# 그러면 4 4 4 4 4 4 4 인 28이 도출된다.

# 입력 조건은 첫째 줄에 N,M,K의 자연수가 주어지며 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다. 
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 입력 예시
# 5 8 3
# 2 4 5 4 6
# 출력 예시
# 46

import sys

num, many, k_overlap = map(int,sys.stdin.readline().split())
num_array = list(map(int,sys.stdin.readline().split()))
sum = 0
a_sum = 0

num_array.sort()
biggest = num_array[-1]
second = num_array[-2] # k_overlap이 1이더라도 이거 둘만 있으면 되기 때문에 이 둘만 저장한다.

a_list = [0 for i in range(k_overlap + 1)] # 이게 큰수가 k_overlap만큼 반복되고 작은거 한 번나오고 다시 큰 수들 반복입니다.
for i in range(k_overlap + 1):
    if i != k_overlap:
        a_list[i] = biggest # 그 k_overlap이 3이면 4개 모임으로 되기에 +1이고 
    else:
        a_list[i] = second # 마지막엔 second가 와야하기 때문이다.

for i in a_list:
    a_sum += i

b = many % len(a_list) # 나머지만큼 더하는데 이건 무조건 큰 수만 있을 수밖에 없다.
a_count = many // len(a_list) # 이건 그 조합들이 몇 번 오는지 확인이다.

sum = a_count * a_sum + biggest * b 

print(sum)

# 드디어 두를 사용한 플레이를 선보였읍니다......
# 책을 펴보았는데 제가 생각한 저 6665 이 아이디어를 사용한게 나와서 매우 뿌듯하였읍니다...