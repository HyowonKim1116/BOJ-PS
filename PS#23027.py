#https://www.acmicpc.net/problem/23027

S = input()

if 'A' in S:
    for i in ['B', 'C', 'D', 'F']:
        S = S.replace(i, 'A')
elif 'B' in S:
    for i in ['C', 'D', 'F']:
        S = S.replace(i, 'B')
elif 'C' in S:
    for i in ['D', 'F']:
        S = S.replace(i, 'C')
else:
    S = 'A' * len(S)

print(S)
