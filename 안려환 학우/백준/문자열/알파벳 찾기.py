import sys

S = list(map(str,sys.stdin.readline().rstrip()))
alphabet = list('abcdefghijklmnopqrstuvwxyz')
total_list = []

for i in range(len(alphabet)):   #애초에 다 -1로 해둔다.
    total_list.append(-1)
    
if len(S) > 100:
    print("You entered wrong length")
else:
    for i in range(len(S)):
        for j in range(len(alphabet)):  #이중 for문을 이용하여 문자열에 어떤 알파벳이 쓰였나 확인
            if S[i] == alphabet[j]: #이렇게 하면 중복이 많더라도 상관없다.
                if total_list[j] == -1:   #이거 안해주면 그 뒤에 중복이 오면
                    total_list[j] = i  #그 다음 문자의 자리로 설정이 된다.

for i in range(len(total_list)):   #걍 리스트로 하게 해주지 아ㅋㅋ
    print(total_list[i], end = ' ') #리스트내용 한 줄 출력하기

#대문자는 좀 봐줍시다. 알아서 넣지 않기로 약속

