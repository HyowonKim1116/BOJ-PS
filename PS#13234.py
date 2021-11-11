#https://www.acmicpc.net/problem/13234

V1, O, V2 = input().split()

if V1 == V2:
    print(V1)
elif O == 'AND':
    print('false')
else:
    print('true')
