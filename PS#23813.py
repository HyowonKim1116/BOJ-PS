#https://www.acmicpc.net/problem/23813

N, answer = input(), 0

for i in range(len(N)):
    answer += int(N[i:] + N[:i])

print(answer)
