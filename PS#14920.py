#https://www.acmicpc.net/problem/14920

C = int(input())
count = 0

while True:
    count += 1
    if C == 1:
        print(count)
        break
    if C % 2:
        C = C * 3 + 1
    else:
        C //= 2
