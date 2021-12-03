#https://www.acmicpc.net/problem/23802

N = int(input())

for _ in range(N):
    print('@' * (N * 5))

for _ in range(N * 4):
    print('@' * N)
