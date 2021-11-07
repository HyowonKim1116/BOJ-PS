#https://www.acmicpc.net/problem/3226

bill = 0

for _ in range(int(input())):
    start, time = input().split()
    h, m = map(int, start.split(':'))
    minute, time = 60 * h + m, int(time)
    if minute in range(420, 1141):
        if (minute + time) in range(420, 1141):
            bill += (10 * time)
        else:
            n = 1140 - minute
            m = time - n
            bill += (10 * n + 5 * m)
    else:
        if (minute + time) in range(420, 1141):
            n = 420 - minute
            m = time - n
            bill += (5 * n + 10 * m)
        else:
            bill += (5 * time)

print(bill)
