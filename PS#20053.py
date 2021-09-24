#https://www.acmicpc.net/problem/20053

T, answer = int(input()), []

for _ in range(T):
    N = int(input())
    M = sorted(list(map(int, input().split())))
    answer.append(f'{M[0]} {M[N - 1]}')

print('\n'.join(answer))
