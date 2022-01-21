#https://www.acmicpc.net/problem/1010

from math import factorial

answer = []

for _ in range(int(input())):
    A, B = map(int, input().split())
    answer.append(factorial(B) // (factorial(A) * factorial(B - A)))

for ans in answer:
    print(ans)
