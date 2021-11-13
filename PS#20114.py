#https://www.acmicpc.net/problem/20114

N, H, W = map(int, input().split())
answer = ['?'] * N

for _ in range(H):
    word = list(input())
    for i in range(0, N*W, W):
        if answer[i//W] != '?':
            continue
        target = set(word[i:i+W])
        target.discard('?')
        if len(target) > 0:
            answer[i//W] = list(target)[0]

print(''.join(answer))
