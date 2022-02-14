#https://www.acmicpc.net/problem/24460

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

while N != 1:
    new = []
    for i in range(0, N, 2):
        item = L[i:i + 2]
        new.append([sorted(item[0][j:j + 2] + item[1][j:j + 2])[1] for j in range(0, N, 2)])
    L = new
    N //= 2

print(L[0][0])
