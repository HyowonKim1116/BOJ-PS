#https://www.acmicpc.net/problem/2010

from sys import stdin, stdout

N = int(stdin.readline())
answer = 1 - N

for _ in range(N):
    answer += int(stdin.readline())

stdout.write('%d'%answer)
