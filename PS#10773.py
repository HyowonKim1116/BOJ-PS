#https://www.acmicpc.net/problem/10773

N = []

for _ in range(int(input())):
    M = int(input())
    if M == 0:
        N.pop()
    else:
        N.append(M)

print(sum(N))
