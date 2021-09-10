#https://www.acmicpc.net/problem/1026

N, answer = int(input()), 0
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse = True)

for i in range(N):
    answer += (A[i] * B[i])

print(answer)
