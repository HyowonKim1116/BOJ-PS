#https://www.acmicpc.net/problem/10707

price = [int(input()) for _ in range(5)]

price1 = price[0] * price[4]
if price[4] <= price[2]:
    price2 = price[1]
else:
    price2 = price[1] + (price[4] - price[2]) * price[3]

print(min(price1, price2))
