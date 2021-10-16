#https://www.acmicpc.net/problem/1668

def display(LIST: list):
    M, answer = 0, 0
    for L in LIST:
        if L > M:
            answer += 1
            M = L
    print(answer)

N = int(input())
trophy = [int(input()) for _ in range(N)]

display(trophy)
display(trophy[::-1])
