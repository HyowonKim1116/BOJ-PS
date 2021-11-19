#https://www.acmicpc.net/problem/9325

answer = []

for _ in range(int(input())):
    price = int(input())
    number = int(input())
    if number == 0:
        answer.append(price)
        continue
    for _ in range(number):
        Q, P = map(int, input().split())
        price += (Q * P)
    answer.append(price)

for ans in answer:
    print(ans)
