#https://www.acmicpc.net/problem/24544

N, M = int(input()), 0
A = list(map(int, input().split()))
B = input().split()

for i in range(N):
    if B[i] == '0':
        M += A[i]

print(f'{sum(A)}\n{M}')
