#https://www.acmicpc.net/problem/16428

A, B = map(int, input().split())
Q, R = A // B, A % B

if R < 0:
    Q += 1
    R = A - B * Q

print(f'{Q}\n{R}')
