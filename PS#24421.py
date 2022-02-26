#https://www.acmicpc.net/problem/24421

N = int(input())
A = list(map(int, input().split()))
answer = 0

for i in range(N - 1, 1, -1):
    for j in range(i - 1):
        for k in range(j + 1, i):
            if A[j] * A[k] == A[i]:
                answer += 1

print(answer)
