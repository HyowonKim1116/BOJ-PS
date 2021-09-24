#https://www.acmicpc.net/problem/15080

H1, M1, S1 = map(int, input().split(':'))
H2, M2, S2 = map(int, input().split(':'))

if S1 > S2:
    S2 += 60
    M2 -= 1

if M1 > M2:
    M2 += 60
    H2 -= 1

if H1 > H2:
    H2 += 24

print((H2 - H1) * 3600 + (M2 - M1) * 60 + S2 - S1)
