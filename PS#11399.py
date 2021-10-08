#https://www.acmicpc.net/problem/11399

N, answer = int(input()), 0
P = sorted(map(int, input().split()))

for i in range(N, 0, -1):
    answer += (P[N - i] * i)

print(answer)
