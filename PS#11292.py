#https://www.acmicpc.net/problem/11292

answer = []

while True:
    N, K = int(input()), 0
    if N == 0:
        break
    for _ in range(N):
        name, height = input().split()
        H = float(height)
        if H > K:
            K = H
            L = [name]
        elif H == K:
            L.append(name)
    answer.append(L)

for ans in answer:
    print(*ans)
