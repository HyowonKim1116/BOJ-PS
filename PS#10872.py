#https://www.acmicpc.net/problem/10872

N = int(input())

if (N == 0) or (N == 1):
    print(1)
else:
    answer = 1
    while N > 1:
        answer *= N
        N -= 1
    print(answer)
