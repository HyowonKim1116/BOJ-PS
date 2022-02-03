#https://www.acmicpc.net/problem/2231

N = int(input())

if N < 11:
    if N % 2 == 0:
        print(N // 2)
    else:
        print(0)
else:
    M = 6
    while True:
        item = M + sum([int(i) for i in str(M)])
        if item == N:
            print(M)
            break
        M += 1
        if M >= N:
            print(0)
            break
