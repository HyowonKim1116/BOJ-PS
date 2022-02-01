#https://www.acmicpc.net/problem/9085

answer = []

for _ in range(int(input())):
    count = int(input())
    value = sum(map(int, input().split()))
    answer.append(str(value))

print('\n'.join(answer))
