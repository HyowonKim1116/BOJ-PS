#https://www.acmicpc.net/problem/20124

M = 0

for _ in range(int(input())):
    name, score = input().split()
    if int(score) > M:
        M = int(score)
        answer = name
    elif int(score) == M:
        answer = sorted([answer, name])[0]

print(answer)
