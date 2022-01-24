#https://www.acmicpc.net/problem/5554

time = sum([int(input()) for _ in range(4)])
print(f'{time // 60}\n{time % 60}')
