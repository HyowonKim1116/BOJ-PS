#https://www.acmicpc.net/problem/23805

N = int(input())

for _ in range(N):
    print('@' * N * 3, end='')
    print(' ' * N, end='')
    print('@' * N)

for _ in range(N * 3):
    print('@' * N, end='')
    print(' ' * N, end='')
    print('@' * N, end='')
    print(' ' * N, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N, end='')
    print(' ' * N, end='')
    print('@' * N * 3)
