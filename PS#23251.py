#https://www.acmicpc.net/problem/23251

from sys import stdin, stdout

answer = []

for _ in range(int(stdin.readline())):
    answer.append(str(int(stdin.readline()) * 23))

stdout.write('\n'.join(answer))
