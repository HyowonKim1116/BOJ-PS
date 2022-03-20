#https://www.acmicpc.net/problem/2442

N = int(input())

for i in range(N - 1, -1, -1):
    star = 2 * (N - i) - 1
    print((' ' * i) + ('*' * star))
