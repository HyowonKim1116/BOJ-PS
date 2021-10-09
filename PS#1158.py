#https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())
number = [i+1 for i in range(N)]
idx, answer = -1, []

for _ in range(N-1):
    idx += K
    try:
        answer.append(str(number.pop(idx)))
        idx -= 1
    except IndexError:
        while True:
            try:
                answer.append(str(number.pop(idx)))
                idx -= 1
                break
            except IndexError:
                idx -= len(number)
answer.append(str(number[0]))

print(f'<{", ".join(answer)}>')
