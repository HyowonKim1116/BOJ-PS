#https://www.acmicpc.net/problem/1629

def main(a, b, c):
    if b == 1:
        return a % c
    x = main(a, b // 2, c)
    if b % 2 == 0:
        return x * x % c
    return x * x * a % c

A, B, C = map(int, input().split())

print(main(A, B, C))
