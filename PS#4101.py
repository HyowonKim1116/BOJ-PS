#https://www.acmicpc.net/problem/4101

number, answer = input(), []

while number != '0 0':
    A, B = map(int, number.split())
    if A > B:
        answer.append('Yes')
    else:
        answer.append('No')
    number = input()

print('\n'.join(answer))
