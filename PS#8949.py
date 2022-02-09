#https://www.acmicpc.net/problem/8949

A, B = input().split()
answer = ''

if len(A) != len(B):
    L = max(len(A), len(B))
    A = f'%0{L}d'%int(A)
    B = f'%0{L}d'%int(B)

for i in range(len(A)):
    answer += str(int(A[i]) + int(B[i]))

print(answer)
