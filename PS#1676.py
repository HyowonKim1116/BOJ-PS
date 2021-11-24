#https://www.acmicpc.net/problem/1676

from math import factorial

F = factorial(int(input()))
count, i = 0, 1

while True:
    number = 10 ** i
    if F % number == 0:
        count += 1
        i += 1
    else:
        print(count)
        break
