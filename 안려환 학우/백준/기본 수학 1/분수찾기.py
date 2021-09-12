import sys

line = 0   #지금 있는 대각선 라인
biggest = 0   #가장 큰 수 

#아 대각선으로 계속 읽는거구나...
X = int(sys.stdin.readline().split(" "))



while X > biggest:
    line += 1
    biggest += line   #그 줄의 수와 가장 큰 수가 같다. 그려보면

#이거 못풀어서 그냥 풀이보고 이해를 했습니다....

gap = biggest - X #이 규칙을 못찾아냈읍니다...

if line % 2 == 0 : #짝수번째 라인일 때 - 대각선
    top = line - gap
    under = gap + 1
else:
    top = gap + 1  #차이는 계속 그 줄의 수중 가장 큰 수와 입력의 차이다.
    under = line - gap  #이게 이 문제의 규칙이다. 

print(f"{top}/{under}")