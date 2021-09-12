#https://www.acmicpc.net/problem/5218

from string import ascii_uppercase

alphabet = {ascii_uppercase[i]: i + 1 for i in range(26)}

T = int(input())
answer = [[] for _ in range(T)]

for t in range(T):
    str1, str2 = input().split()
    subList = answer[t]
    for i in range(len(str1)):
        n1, n2 = alphabet[str1[i]], alphabet[str2[i]]
        if n1 > n2:
            subList.append(str(n2 - n1 + 26))
        else:
            subList.append(str(n2 - n1))

for ans in answer:
    ans = ' '.join(ans)
    print('Distances:', ans)
