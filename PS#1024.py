#https://www.acmicpc.net/problem/1024

N, L = map(int, input().split())
x, y = -1, 0

for i in range(L, 101):
    t = (i * i - i) / 2
    if ((N - t) % i == 0) and ((N - t) // i >= 0):
        x, y = (N - t) // i, i
        break

if x == -1:
    print(-1)
else:
    answer = [int(x + j) for j in range(y)]
    print(*answer)
