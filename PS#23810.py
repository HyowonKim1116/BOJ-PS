#https://www.acmicpc.net/problem/23810

N = int(input())

for _ in range(N):
    print('@' * N * 5)

for _ in range(N):
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)

for _ in range(N * 2):
    print('@' * N)
