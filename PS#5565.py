#https://www.acmicpc.net/problem/5565

price = int(input())

for _ in range(9):
    price -= int(input())

print(price)
