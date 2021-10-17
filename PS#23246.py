#https://www.acmicpc.net/problem/23246

LIST = []

for _ in range(int(input())):
    b, p, q, r = map(int, input().split())
    LIST.append([p * q * r, p + q + r, b])

LIST.sort(key=lambda x: (x[0], x[1], x[2]))

print(f'{LIST[0][2]} {LIST[1][2]} {LIST[2][2]}')
