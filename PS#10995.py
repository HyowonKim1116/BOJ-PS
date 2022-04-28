#https://www.acmicpc.net/problem/10995

N = int(input())
star = ' '.join(['*'] * N)

for i in range(1, N + 1):
    if i % 2:
        print(star)
    else:
        print(' ' + star)
