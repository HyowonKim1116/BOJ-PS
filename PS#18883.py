#https://www.acmicpc.net/problem/18883

N, M = map(int, input().split())
i = 1

for _ in range(N):
    S = [str(j) for j in range(i, i + M)]
    print(' '.join(S))
    i += M
