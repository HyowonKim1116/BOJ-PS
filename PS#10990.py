#https://www.acmicpc.net/problem/10990

N = int(input())
j = 1

print(' ' * (N - 1) + '*')

for i in range(N - 2, -1, -1):
    print(' ' * i + '*' + ' ' * j + '*')
    j += 2
