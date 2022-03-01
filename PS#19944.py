#https://www.acmicpc.net/problem/19944

N, M = map(int, input().split())

if M < 3:
    print('NEWBIE!')
elif N >= M:
    print('OLDBIE!')
else:
    print('TLE!')
