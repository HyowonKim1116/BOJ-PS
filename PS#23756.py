#https://www.acmicpc.net/problem/23756

N = int(input())
P = int(input())
answer = 0

for _ in range(N):
    A = int(input())
    answer += min(abs(A - P), 360 - abs(A - P))
    P = A

print(answer)
