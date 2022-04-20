#https://www.acmicpc.net/problem/10768

A = int(input())
B = int(input())

if (A, B) == (2, 18):
    print('Special')
elif (A == 1) or (A == 2 and B < 18):
    print('Before')
else:
    print('After')
