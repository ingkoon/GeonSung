N = int(input())

count = 0
no_count = 0


for i in range(N):
    word = str(input())
    no_count = 0
    for j in range(len(word)-1):  #j를 피하기 위해서
        if word[j] != word[j+1]: #이후 다른 단어가 왔다면
            new_word = word[j + 1:] #다음 문자부터 새로운 문자열에 추가해준다.
            if new_word.count(word[j]) > 0:
                no_count += 1 #이후 전에 쓰였던 단어가 있다면 그룹 단어가 아니다.
    if no_count == 0:
        count += 1
print(count)



