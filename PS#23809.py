#https://www.acmicpc.net/problem/23809

N = int(input())

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N * 3, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N * 2, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N * 3)

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N * 2, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N * 3, end='')
    print('@' * N)
