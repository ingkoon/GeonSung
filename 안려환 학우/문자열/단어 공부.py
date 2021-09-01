import sys

word = sys.stdin.readline().upper()
final_word = list(word.strip()) #자꾸 개행문자 들어감; input()쓸까 걍?
only_word_list = list(set(final_word))  #중복을 제거한 각 문자들을 가져온다.
cnt_list = []
count = 0
final = {}

for i in only_word_list: #이제 리스트에서 바로 for문 돌리기는 익숙해졌다.
    for j in final_word:
        if i == j:
            count += 1   #문자가 들어가는 만큼 카운트해주기 위해
    cnt_list.append(count)
    
    count = 0  #초기화해줘야 이전 값이 또 쓰이는 일이 없다.
n = 0
for i in only_word_list:
    final[i] = cnt_list[n]  #딕셔너리 키값에 아까 만든 리스트값으로 밸류 채워주기
    n += 1 #또 다른 반복을 위해

biggest = max(final.values())  #이후 제일 큰 값을 찾기 위해
big_count = 0
big_str = ''
for i in final.keys():
    if final[i] == biggest:
        big_count += 1 #가장 중복 많이 된게 무엇인지 알기 위해
        big_str = i   #키값저장 그냥 =한 이유는 위의 카운트가 중복인지 알려줘서 
if big_count > 1: #그 땐 그냥 ?를 쳐줄 것이기 때문이다.
    print("?")
else:
    print(big_str) #제일 중복 많이 된 것이 하나일 땐 바로 그 키값넣은 변수 출력

#여기선 딕셔너리 써보려고 한다. 워드리스트의 값을 키로 cnt_list의 값을 value
#그래서 키 값이 가장 높은걸 출력하고 가장 높은 값이 여러 개면 ?
# if value == max(cnt_list):
#     v_count += 1

# if v_cnt > 1:
#     print("?")
#이후 넣어줄 부분

#zip
#으로도 다음에 풀이를 해볼 예정 일단 딕셔너리 배운거 써보고싶어서
#이번은 딕셔너리로 풀어보았읍니다...