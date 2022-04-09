#https://www.acmicpc.net/problem/13420

answer = []

for _ in range(int(input())):
    Q, A = map(str, input().split(' = '))
    if eval(Q) == int(A):
        answer.append('correct')
    else:
        answer.append('wrong answer')

print('\n'.join(answer))
