#https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
L = [[0] * M for _ in range(N)]

for _ in range(2):
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            L[i][j] += line[j]

for i in range(N):
    print(*L[i])
