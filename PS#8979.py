#https://www.acmicpc.net/problem/8979

from sys import stdin

N, K = map(int, stdin.readline().split())
rank = 1

L = [list(map(int, stdin.readline().split())) for _ in range(N)]
L.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)

for i in range(N):
    if L[i][0] == K:
        print(rank)
        break
    elif L[i][1:] != L[i + 1][1:]:
        rank = i + 2
