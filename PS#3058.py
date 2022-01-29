#https://www.acmicpc.net/problem/3058

SUM, MIN, T = [], [], int(input())

for _ in range(T):
    number = list(map(int, input().split()))
    even = []
    for num in number:
        if num % 2 == 0:
            even.append(num)
    SUM.append(sum(even))
    MIN.append(min(even))

for i in range(T):
    print(SUM[i], MIN[i])
