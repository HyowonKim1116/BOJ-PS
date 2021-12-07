#https://www.acmicpc.net/problem/23806

N = int(input())

for _ in range(N):
    print('@' * N * 5)

for _ in range(N * 3):
    print('@' * N, end='')
    print(' ' * N * 3, end='')
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)
