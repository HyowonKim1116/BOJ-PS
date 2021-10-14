#https://www.acmicpc.net/problem/14659

N = int(input())
M = list(map(int, input().split()))
MAX = 0

for i in range(N-1):
    count = 0
    for j in range(i+1, N):
        if M[i] < M[j]:
            break
        count += 1
    MAX = max(MAX, count)

print(MAX)
