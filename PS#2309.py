#https://www.acmicpc.net/problem/2309

height = [int(input()) for _ in range(9)]
total, answer = sum(height), height

for h in height[:-1]:
    answer.remove(h)
    value = total - h - 100
    try:
        answer.remove(value)
        break
    except:
        answer.append(h)

for ans in sorted(answer):
    print(ans)
