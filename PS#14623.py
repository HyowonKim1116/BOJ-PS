#https://www.acmicpc.net/problem/14623

B1, B2 = input(), input()
answer = bin(int(B1, 2) * int(B2, 2))

print(answer[2:])
