#https://www.acmicpc.net/problem/3181

X = list(input().split())
answer = X.pop(0)[0]
word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

for x in X:
    if x not in word:
        answer += x[0]

print(answer.upper())
