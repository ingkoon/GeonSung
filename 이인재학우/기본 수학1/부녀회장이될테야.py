import sys

user_input = int(sys.stdin.readline())

for b in range(user_input):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    people = [ i for i in range(1, n+1)]
    for q in range(k):

        for j in range(1,n):

            people[j] += people[j-1]

    print(people[-1])