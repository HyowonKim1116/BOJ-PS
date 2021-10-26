#https://www.acmicpc.net/problem/2721

number = [int(input()) for _ in range(int(input()))]

for n in number:
    answer = 0
    for i in range(1, n+1):
        answer += (i * (i+1) * (i+2) // 2)
    print(answer)
