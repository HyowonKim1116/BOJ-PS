#https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())
X, Y, Z, year = 1, 1, 1, 1

while (E, S, M) != (X, Y, Z):
    X += 1; Y += 1; Z += 1; year += 1
    if X > 15:
        X = 1
    if Y > 28:
        Y = 1
    if Z > 19:
        Z = 1

print(year)
