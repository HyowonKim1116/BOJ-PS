#https://www.acmicpc.net/problem/24508

N, K, T = map(int, input().split())
A = sorted(list(map(int, input().split())))

if sum(A) % K:
    print('NO')
else:
    M = sum(A) // K
    if sum(A[:-M]) > T:
        print('NO')
    else:
        print('YES')
