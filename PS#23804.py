#https://www.acmicpc.net/problem/23804

N = int(input())

for _ in range(N):
    print('@' * N * 5)

for _ in range(3 * N):
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)
