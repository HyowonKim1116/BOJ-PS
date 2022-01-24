#https://www.acmicpc.net/problem/10040

N, M = map(int, input().split())

cost = [int(input()) for _ in range(N)]
vote = [0] * N

for i in range(M):
    S = int(input())
    for j in range(N):
        if S >= cost[j]:
            vote[j] += 1
            break

print(vote.index(max(vote)) + 1)
