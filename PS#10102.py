#https://www.acmicpc.net/problem/10102

V, vote = input(), input()
A = vote.count('A')
B = vote.count('B')

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')
