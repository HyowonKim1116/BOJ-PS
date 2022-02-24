#https://www.acmicpc.net/problem/11021

count, number = int(input()), dict()

for i in range(1, count + 1):
    number[i] = sum(map(int, input().split()))

for key in number.keys():
    print(f'Case #{key}: {number[key]}')
