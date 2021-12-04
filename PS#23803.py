#https://www.acmicpc.net/problem/23803

N = int(input())

for _ in range(N * 4):
    print('@' * N)

for _ in range(N):
    print('@' * N * 5)
