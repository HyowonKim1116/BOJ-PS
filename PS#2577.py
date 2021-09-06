#https://www.acmicpc.net/problem/2577

result = 1
for _ in range(3):
    result *= int(input())

result = str(result)
for i in range(10):
    print(result.count(str(i)))
