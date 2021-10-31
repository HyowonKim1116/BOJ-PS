#https://www.acmicpc.net/problem/4388

number1, number2 = [], []

while True:
    N1, N2 = input().split()
    if (N1, N2) == ('0', '0'):
        break
    number1.append(N1)
    number2.append(N2)

for i in range(len(number1)):
    A, B = number1[i], number2[i]
    M = max(len(A), len(B))
    A, B = f'%0{M}d'%int(A), f'%0{M}d'%int(B)
    j, check, answer = 0, 0, 0
    
    for _ in range(M):
        j -= 1
        if (int(A[j]) + int(B[j]) + check >= 10):
            check = 1
            answer += 1
        else:
            check = 0
    
    print(answer)
