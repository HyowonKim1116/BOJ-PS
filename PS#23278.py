#https://www.acmicpc.net/problem/23278

N, L, H = map(int, input().split())
score = sorted(list(map(int, input().split())))

print(sum(score[L:N-H]) / (N-L-H))
