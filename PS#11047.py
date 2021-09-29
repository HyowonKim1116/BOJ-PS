#https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
answer = 0

for i in reversed(coin):
    if i <= K:
        answer += (K // i)
        K %= i
        if K == 0:
            print(answer)
            break
