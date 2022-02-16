#https://www.acmicpc.net/problem/2455

number = [list(map(int, input().split())) for _ in range(4)]
answer, value = 0, number[0][1]

for i in range(1, 4):
    result = value + number[i][1] - number[i][0]
    value = result
    answer = max(answer, result)

print(answer)
