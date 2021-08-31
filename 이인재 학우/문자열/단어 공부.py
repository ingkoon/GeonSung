# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


import sys

# 단어 입력
user_input = sys.stdin.read().upper()
# 중복 제거한 값을 리스트로 지정
keyWord = list(set(user_input))

# 결과 반환을 위한 배열 선언
freq = []

# 반복문을 통해 사용자 입력 부분을 카운트 후 배열에 출력
for i in keyWord:
    cnt = user_input.count(i)
    freq.append(cnt)

# 조건문을 사용하여 모든 값이 동일할 경우 ? 출력
if freq.count(max(freq)) > 1: 
    print('?')
# 이외에는 값 출력
else:
    print(keyWord[freq.index(max(freq))])