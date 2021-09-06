#https://www.acmicpc.net/problem/1032

N, answer = int(input()), ''
file = [input() for _ in range(N)]

for i in range(len(file[0])):
    S = {f[i] for f in file}
    if len(S) == 1:
        answer += list(S)[0]
    else:
        answer += '?'

print(answer)
