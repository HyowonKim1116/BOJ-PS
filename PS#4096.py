#https://www.acmicpc.net/problem/4096

answer = []

while True:
    T = input()

    if T == '0':
        print('\n'.join(answer))
        break

    L, N = len(T), int(T)

    while f'%0{L}d'%N != (f'%0{L}d'%N)[::-1]:
        N += 1
    
    answer.append(str(N - int(T)))
