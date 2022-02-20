#https://www.acmicpc.net/problem/17219

from sys import stdin

N, M = map(int, stdin.readline().split())
memo = dict()

for _ in range(N):
    site, password = stdin.readline().split()
    memo[site] = password

answer = [memo[stdin.readline().rstrip()] for _ in range(M)]

print('\n'.join(answer))
