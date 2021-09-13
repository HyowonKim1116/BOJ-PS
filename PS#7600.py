#https://www.acmicpc.net/problem/7600

from string import ascii_lowercase

answer = []

while True:
    S = input().lower()

    if S == '#':
        break

    L = list(set(''.join(S.split())))
    count = 0
    
    for i in L:
        if i in ascii_lowercase:
            count += 1
    
    answer.append(str(count))

print('\n'.join(answer))
