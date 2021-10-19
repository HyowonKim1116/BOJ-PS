#https://www.acmicpc.net/problem/10814

from sys import stdin

N = int(stdin.readline())
A = [stdin.readline().split() for _ in range(N)]
answer = sorted(A, key=lambda x: int(x[0]))

for ans in answer:
    print(*ans)
