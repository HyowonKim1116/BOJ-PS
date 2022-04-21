#https://www.acmicpc.net/problem/10214

answer = []

for _ in range(int(input())):
    scoreY, scoreK = 0, 0
    for _ in range(9):
        Y, K = map(int, input().split())
        scoreY += Y
        scoreK += K
    if scoreY > scoreK:
        answer.append('Yonsei')
    elif scoreY < scoreK:
        answer.append('Korea')
    else:
        answer.append('Draw')

print('\n'.join(answer))
