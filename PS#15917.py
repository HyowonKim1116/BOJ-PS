#https://www.acmicpc.net/problem/15917

from sys import stdin

def main(n: int):
    if n < 3:
        return 1
    while True:
        if n % 2 != 0:
            return 0
        n //= 2
        if n == 2:
            return 1

for i in [int(stdin.readline()) for _ in range(int(stdin.readline()))]:
    print(main(i))
