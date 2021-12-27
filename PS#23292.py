#https://www.acmicpc.net/problem/23292

birth = input()
answer, rhythm = 99991231, 0

for _ in range(int(input())):
    date = input()
    ys, ms, ds = 0, 0, 0
    for i in range(4):
        ys += (int(birth[i]) - int(date[i])) ** 2
    for i in range(4, 6):
        ms += (int(birth[i]) - int(date[i])) ** 2
    for i in range(6, 8):
        ds += (int(birth[i]) - int(date[i])) ** 2
    target = ys * ms * ds
    if target > rhythm:
        rhythm = target
        answer = int(date)
    elif (target == rhythm) and (answer > int(date)):
        answer = int(date)

print(answer)
