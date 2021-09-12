import sys

#아스키코드로 바꿔주는 함수를 사용해야 한다.
asc = sys.stdin.readline().rstrip()
print(ord(asc))

#sys.stdin.read 를 쓰니까 에러가 났다.
#에러메세지:TypeError: ord() expected a character, but string of length 2 found
#인터넷에 sys.stdin.readline이 어떻게 작동되나 확인해봐야 겠다.
#sys.stdin.readline 은 마지막에 개행문자를 포함한 값을
#리턴해서 타입에러가 뜬 것 같다.
#그러니 마지막에 rstrip()을 적용해야 한다.
#이 rstrip()메소드는 문자열의 끝을 삭제하는 기능을 갖고있다.