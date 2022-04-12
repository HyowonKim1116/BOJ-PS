#https://www.acmicpc.net/problem/9012

def main(s: str):
    x, y = 0, 0
    for i in s:
        if i == '(':
            x += 1
        else:
            y += 1
        if x < y:
            return 'NO'
    if x == y:
        return 'YES'
    else:
        return 'NO'

answer = [main(input()) for _ in range(int(input()))]

print('\n'.join(answer))
