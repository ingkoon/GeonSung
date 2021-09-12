import sys

T = int(sys.stdin.readline())


input_list = []
final = ''
final_list = [0 for i in range(T)] #리스트 컴프리헨션 드디어 써먹었읍니다...

#hwn 입력받기
for i in range(T):
    h, w, n = map(int,sys.stdin.readline().split(" ")) #이거 달팽이 때 대문자해서 스트레스받았음
    # h = height 층수 w = width 가로줄 n = number 몇 번째 손님인지
    if h * w < n:
        print("error")
    else:
        input_list.append([h,w,n])

#이제 호실 찾기
for i in range(T): #입력받은 만큼 반복인데
    w_count = input_list[i][2] // input_list[i][0] #이게 30층씩 있으니 그걸로 나눠서 몇
    if input_list[i][2] % input_list[i][0] != 0: #번째 줄인지 확인인데 나머지 있으면 하나더
        w_count += 1
        N = input_list[i][2] % input_list[i][0] #이 나머지를 가져다가 써야하기에
        if len(str(w_count)) < 2: #앞 카운트가 한 자리면 중간에 0들어가야됨 
            final = str(N) + '0' + str(w_count)
        else:
            final = str(N) + str(w_count) #두 자리수면 이거 중간에 0빼야 한다.
    else: #나눠 떨어지는 수면 꼭대기층으로 가게 된다. 이거 안해주면 0층이 생겨버린다.
        if len(str(w_count)) < 2: #앞 카운트가 한 자리면 중간에 0들어가야됨 
            final = str(input_list[i][0]) + '0' + str(w_count) 
        else:
            final = str(input_list[i][0]) + str(w_count) #두 자리수면 이거 중간에 0빼야 한다.
        
        #이게 h이다.
    final_list[i] = final
    w_count = 0

# w_count = n // h
# if n % h != 0:
#     w_count += 1
# final = n % h + w_count 이 모양을 만들어주었읍니다.

for i in range(T):
    print(final_list[i])



