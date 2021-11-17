#https://www.acmicpc.net/problem/9493

answer = []

while True:
    M, A, B = map(int, input().split())
    if M == 0:
        break
    time = 3600 * M / A - 3600 * M / B
    hour = time // 3600
    minute = (time % 3600) // 60
    second = round(time % 60)
    answer.append('%d:%02d:%02d'%(hour, minute, second))

print('\n'.join(answer))
