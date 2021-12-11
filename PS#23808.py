#https://www.acmicpc.net/problem/23808

N = int(input())

for _ in range(N * 2):
    print('@' * N, end='')
    print(' ' * N * 3, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N * 3, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)
