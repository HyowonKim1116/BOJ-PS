#https://www.acmicpc.net/problem/10991

N = int(input())
j = 0

for i in range(N - 1, -1, -1):
    j += 1
    star = ['*' for _ in range(j)]
    print(' ' * i + ' '.join(star))
