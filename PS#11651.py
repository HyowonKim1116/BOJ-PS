#https://www.acmicpc.net/problem/11651

number = [list(map(int, input().split())) for _ in range(int(input()))]
number.sort(key = lambda x: (x[1], x[0]))

for num in number:
    print(*num)
