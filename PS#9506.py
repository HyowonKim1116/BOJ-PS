#https://www.acmicpc.net/problem/9506

answer = []

while True:
    N = int(input())
    if N == -1:
        break
    factor = [i for i in range(1, N) if N % i == 0]
    total = sum(factor)
    if N == total:
        string = list(map(str, factor))
        result = str(N) + ' = ' + ' + '.join(string)
    else:
        result = f'{N} is NOT perfect.'
    answer.append(result)

print('\n'.join(answer))
