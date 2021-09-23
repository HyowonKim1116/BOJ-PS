#https://www.acmicpc.net/problem/17206

T = int(input())
N = map(int, input().split())

for n in N:
    k3 = n // 3
    k7 = n // 7
    answer = 1.5 * k3 * (k3 + 1) + 3.5 * k7 * (k7 + 1)
    
    if n > 20:
        k21 = n // 21
        answer -= (10.5 * k21 * (k21 + 1))
    
    print(int(answer))
