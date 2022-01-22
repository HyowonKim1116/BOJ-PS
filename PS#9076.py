#https://www.acmicpc.net/problem/9076

answer = []

for _ in range(int(input())):
    score = sorted(list(map(int, input().split())))
    score.pop(0)
    score.pop(3)
    if score[2] - score[0] < 4:
        answer.append(str(sum(score)))
    else:
        answer.append('KIN')

print('\n'.join(answer))
