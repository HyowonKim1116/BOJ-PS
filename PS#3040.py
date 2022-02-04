#https://www.acmicpc.net/problem/3040

N = [int(input()) for _ in range(9)]
M = sum(N) - 100

for n in N:
    m = M - n
    if m in N:
        N.remove(n)
        N.remove(m)
        break

for i in N:
    print(i)
