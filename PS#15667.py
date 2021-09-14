#https://www.acmicpc.net/problem/15667

N = int(input()) - 1
for i in range(N // 2, 0, -1):
    if i ** 2 + i == N:
        print(i)
        break
