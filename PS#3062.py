#https://www.acmicpc.net/problem/3062

answer = []

for _ in range(int(input())):
    number = input()
    result = str(int(number) + int(number[::-1]))
    if result == result[::-1]:
        answer.append('YES')
    else:
        answer.append('NO')

print('\n'.join(answer))
