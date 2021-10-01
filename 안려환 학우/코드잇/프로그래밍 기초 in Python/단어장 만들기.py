alpha = 'a'

def voca(alpha):
    alpha = input('영어 단어를 입력하세요: ')
    if alpha != 'q':
        with open('안려환 학우\\코드잇\\프로그래밍 기초 in Python\\data\\vocabulary.txt','a') as f:
            f.write(alpha)
            alpha = input('한국어 뜻을 입력하세요: ')
            korea = ': ' + alpha + '\n'
            f.write(korea)
            voca(alpha)

voca(alpha)

# with open('안려환 학우\\코드잇\\프로그래밍 기초 in Python\\data\\vocabulary.txt','r') as d:
#         for i in d:
#             print(i.strip())
# 이건 코딩할 때 잘 입력되고 있는지 확인하기 위함.