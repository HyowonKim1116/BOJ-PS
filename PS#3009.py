#https://www.acmicpc.net/problem/3009

number1, number2 = [], []

for _ in range(3):
    num1, num2 = map(int, input().split())
    number1.append(num1)
    number2.append(num2)

x = min(number1, key = number1.count)
y = min(number2, key = number2.count)

print(x, y)
