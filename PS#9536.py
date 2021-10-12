#https://www.acmicpc.net/problem/9536

answer = []

for _ in range(int(input())):
    S = input().split()
    while True:
        A = input()
        if A == 'what does the fox say?':
            break
        A = A.split()[2]
        while True:
            try:
                S.remove(A)
            except ValueError:
                break
    answer.append(' '.join(S))

print('\n'.join(answer))
