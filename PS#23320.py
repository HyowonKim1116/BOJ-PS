#https://www.acmicpc.net/problem/23320

N = int(input())
score = sorted(list(map(int, input().split())))
X, Y = map(int, input().split())

n1 = int(N * X * 0.01)

if Y in score:
    idx = score.index(Y)
    n2 = N - idx
else:
    n2 = 0
    for i in range(N):
        if score[i] >= Y:
            n2 = N - i
            break

print(n1, n2)
