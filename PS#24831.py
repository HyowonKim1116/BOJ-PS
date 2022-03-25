#https://www.acmicpc.net/problem/24831

answer = []

for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    if (y - x) % (a + b):
        answer.append('-1')
    else:
        answer.append(str((y - x) // (a + b)))

print('\n'.join(answer))
