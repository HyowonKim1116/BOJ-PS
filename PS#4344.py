#https://www.acmicpc.net/problem/4344

answer = []

for _ in range(int(input())):
    score = list(map(int, input().split()))
    total, count = score.pop(0), 0
    average = sum(score) / total
    for s in score:
        if s > average:
            count += 1
    answer.append(count / total * 100)

for ans in answer:
    print('%.3f'%ans + '%')
