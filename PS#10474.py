#https://www.acmicpc.net/problem/10474

answer = []

while True:
    A, B = map(int, input().split())

    if (A == 0) and (B == 0):
        break

    answer.append([A // B, A % B, B])

for ans in answer:
    print(f'{ans[0]} {ans[1]} / {ans[2]}')
