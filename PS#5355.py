#https://www.acmicpc.net/problem/5355

N = int(input())
answer = []

for _ in range(N):
    X = input().split()
    A = float(X.pop(0))
    for i in X:
        if i == '@':
            A *= 3
        elif i == '%':
            A += 5
        else:
            A -= 7
    answer.append(A)

for ans in answer:
    print('%.2f'%ans)
