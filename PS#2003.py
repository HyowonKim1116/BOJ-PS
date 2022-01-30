#https://www.acmicpc.net/problem/2003

from sys import stdin

N, M = map(int, stdin.readline().split())
number = list(map(int, stdin.readline().split()))
count, x, y, item = 0, 0, 1, number[0]

while N > x:
    if item == M:
        item -= number[x]
        count += 1
        x += 1
    if (N == y) and (item < M):
        break
    if item < M:
        item += number[y]
        y += 1
    elif item > M:
        item -= number[x]
        x += 1

print(count)
