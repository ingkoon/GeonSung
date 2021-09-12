import sys

a, b, c = map(int,sys.stdin.readline().split(" ")) #자꾸 에러떠서 결국 돌아옴...
final = 0  #이거 안해주니까 런타임 에러뜬다.
if b >= c:
    print(-1)
else:  #while로 계산하니까 시간이 너무 오래걸림. - 뻘짓임 변수 세 개가 이미 주어진 상황 하나씩 대입할 필요 없음 그대로 계산
    final = int(a/(c - b) + 1)  #변수 세 개가 주어진 상황에서 
    print(final) #그대로 식 계산하면 알고싶던 i를 알 수 있다.
    # +1은 처음 카운트가 1부터 시작되기 때문이다.