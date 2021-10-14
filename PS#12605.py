#https://www.acmicpc.net/problem/12605

N = int(input())
S = [input().split()[::-1] for _ in range(N)]

for i in range(N):
    print(f'Case #{i+1}: {" ".join(S[i])}')
