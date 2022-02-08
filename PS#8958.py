#https://www.acmicpc.net/problem/8958

score = []

for _ in range(int(input())):
    result = input()
    total, add = 0, 0
    for r in result:
        if r == 'O':
            add += 1
            total += add
        else:
            add = 0
    score.append(str(total))

print('\n'.join(score))
