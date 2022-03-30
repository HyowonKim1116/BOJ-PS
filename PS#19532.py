#https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())
x = (c * e - b * f) // (a * e - b * d)

try:
    y = (c - a * x) // b
except ZeroDivisionError:
    y = (f - d * x) // e

print(x, y)
