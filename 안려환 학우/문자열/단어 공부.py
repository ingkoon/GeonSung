import sys

word = sys.stdin.readline().upper()
final_word = list(word.strip()) #자꾸 개행문자 들어감; input()쓸까 걍?
only_word_list = list(set(final_word))  #중복을 제거한 각 문자들을 가져온다.
cnt_list = []
count = 0

print(only_word_list)
for i in only_word_list: #이제 리스트에서 바로 for문 돌리기는 익숙해졌다.
    for j in final_word:
        if i == j:
            count += 1
    cnt_list.append(count)
    count = 0

print(cnt_list)
#여기선 딕셔너리 써보려고 한다. 워드리스트의 값을 키로 cnt_list의 값을 value
#그래서 키 값이 가장 높은걸 출력하고 가장 높은 값이 여러 개면 ?
# if value == max(cnt_list):
#     v_count += 1

# if v_cnt > 1:
#     print("?")
#이후 넣어줄 부분