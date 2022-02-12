#https://www.acmicpc.net/problem/7785

N = int(input())
answer = {}

for _ in range(N):
    name, state = input().split()
    if state == 'enter':
        answer[name] = 'enter'
    else:
        del answer[name]

print('\n'.join(sorted(answer, reverse = True)))
