#https://www.acmicpc.net/problem/10156

K, N, M = map(int, input().split())
result = K * N - M

if result > 0:
    print(result)
else:
    print(0)
