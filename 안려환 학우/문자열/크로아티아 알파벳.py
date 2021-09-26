word = str(input())
croatian = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
real_count = 0
dz = 0
#지렸다.

for i in range(len(croatian)): #크로아티안 알파벳이 있나 확인이 더 좋다.
    if croatian[i] in word:
        count += word.count(croatian[i]) #나머지 단어들관련 체크
dz = word.count(croatian[2])
real_count = count - dz  #count에서 dz 와 z 가 중복 체크가 되었다.
alpha_num = len(word) - real_count * 2 -dz #크로아티안 다 두자리로 dz은 3자리라 마지막에 dz빼줘야 한다.


print(alpha_num + real_count)# 장장 4시간 걸려서 풀었읍니다.


#검색해보니 다른 분들은 replace를 이용해서 풀었더군요. 각 크로아티아문자 자체를 i로 동일하게 바꾸어서
#그렇게 하게 되면 dz 와 z의 중복문제는 자연스럽게 해결이 되게 됩니다.
#애초에 그럴 생각 자체를 못하고 저는 어떻게 생각하고 풀었냐면
#입력받은 문자열에 크로아티안 알파벳의 갯수를 셉니다. 
#크로아티안 알파벳 길이들은 2이고 dz=만 3입니다.
#그래서 그 dz=의 수를 세어주게 되면 전체 크로아티안 알파벳이 얼마나 들었는지 알 수 있게 됩니다.
#여기서 또 확인해야할 것은 dz= 와 z=는 중복된다는 점입니다. 그래서 dz=의 수만큼 빼주어야 중복을 제거할 수 있습니다.




