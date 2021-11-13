#https://www.acmicpc.net/problem/20359

n, p = int(input()), 0

while n > 1:
    if n % 2 == 0:
        n //= 2
        p += 1
    else:
        break

print(n, p)
