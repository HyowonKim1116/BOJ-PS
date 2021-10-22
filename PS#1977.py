#https://www.acmicpc.net/problem/1977

from math import ceil, floor, sqrt

M = ceil(sqrt(int(input())))
N = floor(sqrt(int(input())))

if M > N:
    print(-1)
else:
    print(sum([i * i for i in range(M, N+1)]))
    print(M * M)
