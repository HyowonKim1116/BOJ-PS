#https://www.acmicpc.net/problem/10992

N = int(input())

print(' ' * (N - 1) + '*')

if N > 1:
    j = N - 2
    for i in range(1, 2 * N - 3, 2):
        print(' ' * j + '*' + ' ' * i + '*')
        j -= 1
    print('*' * (2 * N - 1))
