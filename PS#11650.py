#https://www.acmicpc.net/problem/11650

from sys import stdin, stdout

pos = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
answer = sorted(pos, key = lambda x: (x[0], x[1]))

for ans in answer:
    stdout.write(f'{ans[0]} {ans[1]}\n')
