#https://www.acmicpc.net/problem/22938

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = (x1 - x2) ** 2 + (y1 - y2) ** 2
r = (r1 + r2) ** 2

print('YES' if d < r else 'NO')
