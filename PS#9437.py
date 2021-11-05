#https://www.acmicpc.net/problem/9437

answer = []

while True:
    try:
        N, P = map(int, input().split())
        p1 = N - P + 1
        m = min(P, p1)
        if m % 2:
            p2 = m + 1
        else:
            p2 = m - 1
        p3 = N - p2 + 1
        answer.append(sorted([p1, p2, p3]))
    except ValueError:
        for ans in answer:
            print(*ans)
        break
