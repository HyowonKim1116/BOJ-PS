#https://www.acmicpc.net/problem/2408

S = ''

for _ in range(2 * int(input()) - 1):
    I = input()
    if I == '/':
        I = '//'
    S += I

print(eval(S))
