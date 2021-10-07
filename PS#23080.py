#https://www.acmicpc.net/problem/23080

K, S = int(input()), input()
i = 0

while True:
    try:
        print(S[i], end = '')
        i += K
    except IndexError:
        break
