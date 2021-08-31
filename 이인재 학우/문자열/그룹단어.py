# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

import sys

# 단어의 개수 입력
userInput = int(sys.stdin.readline())

# 최종 결과값은 그룹단어가 아닌 단어를 검출 할 때마다 1씩 감소시킬 것
result = userInput

# 단어의 개수 만큼 반복
for i in range(userInput):
    # 단어 입력
    word = sys.stdin.readline()
    # 줄바꿈 제거
    word = word[:-1]
    # 반복문을 통해서 체크
    for j in range(len(word)-1):
        # 다음 글자와 같을 경우 무시
        if word[j] == word[j+1]:
            continue
        # 해당 글자가 이후의 문자열에서 검출 될 경우 결과값에서 1 감소
        elif word[j] in word[j+1:]:
            result -= 1
            break

# 결과 출력
print(result)



    