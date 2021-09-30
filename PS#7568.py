#https://www.acmicpc.net/problem/7568

N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    item1 = num[i]
    for j in range(i+1, N):
        item2 = num[j]
        if (item1[0] > item2[0]) and (item1[1] > item2[1]):
            rank[j] += 1
        elif (item1[0] < item2[0]) and (item1[1] < item2[1]):
            rank[i] += 1

print(' '.join(list(map(str, rank))))
