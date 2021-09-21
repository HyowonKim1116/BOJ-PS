#https://www.acmicpc.net/problem/5217

number = [int(input()) for _ in range(int(input()))]

for num in number:
    if num % 2:
        item = num // 2 + 1
    else:
        item = num // 2
    
    result = [f'{j} {num - j}' for j in range(1, item)]
    print(f'Pairs for {num}: {", ".join(result)}')
