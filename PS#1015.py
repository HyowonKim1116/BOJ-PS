#https://www.acmicpc.net/problem/1015

N = int(input())
A = list(map(int, input().split()))
S, result = sorted(A), []

for i in A:
    idx = S.index(i)
    result.append(idx)
    S[idx] = -1

print(*result)
