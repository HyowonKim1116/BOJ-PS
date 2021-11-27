#https://www.acmicpc.net/problem/1920

from sys import stdin, stdout

N = input()
numN = set(stdin.readline().split())
M = input()
numM = stdin.readline().split()

for n in numM:
    if n in numN:
        stdout.write('1\n')
    else:
        stdout.write('0\n')
