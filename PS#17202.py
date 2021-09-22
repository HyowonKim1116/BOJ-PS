#https://www.acmicpc.net/problem/17202

A, B, S = input(), input(), ''

for i in range(8):
    S += (A[i] + B[i])

while True:
    if len(S) == 2:
        print(S)
        break

    K = ''
    for i in range(len(S) - 1):
        K += str(int(S[i]) + int(S[i+1]))[-1]
    S = K
