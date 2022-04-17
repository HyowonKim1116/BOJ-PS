#https://www.acmicpc.net/problem/10809

from string import ascii_lowercase

string = input()
lowercase = list(ascii_lowercase)
result = []

for i in lowercase:
    try:
        result.append(string.index(i))
    except:
        result.append(-1)

print(*result)
