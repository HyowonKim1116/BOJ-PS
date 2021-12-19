#https://www.acmicpc.net/problem/23841

N, M = map(int, input().split())
answer = []

for _ in range(N):
    P = list(input())
    for i in range(M):
        if P[i] != '.':
            P[M-i-1] = P[i]
    answer.append(''.join(P))

print('\n'.join(answer))
