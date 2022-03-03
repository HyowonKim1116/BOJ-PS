#https://www.acmicpc.net/problem/1100

answer = 0

for i in range(8):
    L = list(input())
    if i % 2:
        answer += L[1::2].count('F')
    else:
        answer += L[0::2].count('F')

print(answer)
