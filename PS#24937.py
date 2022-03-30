#https://www.acmicpc.net/problem/24937

N = int(input()) % 10
S = 'SciComLove'

print(S[N:] + S[:N])
