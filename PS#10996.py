#https://www.acmicpc.net/problem/10996

N = int(input())

if N == 1:
    print('*')
elif N % 2:
    star = ['*'] * (N // 2 + 1)
    for i in range(2 * N):
        if i % 2:
            print(' ' + ' '.join(star[:-1]))
        else:
            print(' '.join(star))
else:
    star = ['*'] * (N // 2)
    for i in range(2 * N):
        if i % 2:
            print(' ' + ' '.join(star))
        else:
            print(' '.join(star))
