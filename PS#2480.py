#https://www.acmicpc.net/problem/2480

number = list(map(int, input().split()))
unique = set(number)

if len(unique) == 1:
    print(10000 + number[0] * 1000)
elif len(unique) == 2:
    for n in unique:
        number.remove(n)
    print(1000 + number[0] * 100)
else:
    print(max(number) * 100)
