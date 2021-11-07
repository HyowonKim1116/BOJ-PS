#https://www.acmicpc.net/problem/23348

score = []
A, B, C = map(int, input().split())

for _ in range(int(input())):
    x, y, z = 0, 0, 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        x += a
        y += b
        z += c
    score.append(x*A + y*B + z*C)

print(max(score))
