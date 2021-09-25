#https://www.acmicpc.net/problem/21567

N = str(int(input()) * int(input()) * int(input()))

for i in range(10):
    print(N.count(str(i)))
