#https://www.acmicpc.net/problem/23628

Sy, Sm, Sd = map(int, input().split())
Ey, Em, Ed = map(int, input().split())

d, m, y = Ed - Sd, Em - Sm, Ey - Sy

if d < 0:
    d += 30
    m -= 1

if m < 0:
    m += 12
    y -= 1

days = 360 * y + 30 * m + d
N, M = days // 360, days // 30

if N % 2:
    A = int(N / 2)
    B = 15 * N + A * (A + 1) - A
else:
    A = (N // 2) - 1
    B = 15 * N + A * (A + 1)

if M > 36:
    M = 36

print(B, M)
print(f'{days}days')
