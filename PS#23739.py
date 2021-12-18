#https://www.acmicpc.net/problem/23739

N = int(input())
answer, check = 0, 0

for _ in range(N):
    T = int(input())
    check += T
    if check < 30:
        answer += 1
        continue
    if (check - 30) <= (T / 2):
        answer += 1
    check = 0

print(answer)
