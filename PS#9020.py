#https://www.acmicpc.net/problem/9020

def isPrime(num: int):
    if num < 4:
        return True
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
answer = []

for _ in range(T):
    n = int(input())
    x, y = n // 2, n // 2
    while (isPrime(x) == False) or (isPrime(y) == False):
        x -= 1
        y += 1
    answer.append([x, y])

for i in range(T):
    print(*answer[i])
