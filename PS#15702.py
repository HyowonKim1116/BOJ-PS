#https://www.acmicpc.net/problem/15702

N, M = map(int, input().split())
S = list(map(int, input().split()))
rank = dict()

for _ in range(M):
    grade = input().split()
    number = int(grade.pop(0))
    score = 0
    for i in range(N):
        if grade[i] == 'O':
            score += S[i]
    rank[number] = score

answer = sorted(rank.items(), key=lambda x: (-x[1], x[0]))[0]
print(answer[0], answer[1])
