#https://www.acmicpc.net/problem/9093

answer = []

for _ in range(int(input())):
    STRING = input().split()
    reverse = []
    for s in STRING:
        reverse.append(s[::-1])
    answer.append(' '.join(reverse))

for ans in answer:
    print(ans)
