#https://www.acmicpc.net/problem/1546

N = int(input())
score = list(map(int, input().split()))
highest = max(score)

for i in range(N):
    score[i] *= (100 / highest)

print(sum(score) / N)
