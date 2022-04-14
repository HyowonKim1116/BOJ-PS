#https://www.acmicpc.net/problem/1292

A, B = map(int, input().split())
L = []

for i in range(1, B + 1):
    L.extend([i for _ in range(i)])

print(sum(L[A - 1:B]))
