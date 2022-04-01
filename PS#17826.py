#https://www.acmicpc.net/problem/17826

score = list(map(int, input().split()))
rank = score.index(int(input())) + 1

if rank < 6:
    print('A+')
elif rank < 16:
    print('A0')
elif rank < 31:
    print('B+')
elif rank < 36:
    print('B0')
elif rank < 46:
    print('C+')
elif rank < 49:
    print('C0')
else:
    print('F')
