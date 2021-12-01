#https://www.acmicpc.net/problem/23746

string, origin = dict(), ''

for _ in range(int(input())):
    x, y = input().split()
    string[y] = x

for i in input():
    origin += string[i]

n1, n2 = map(int, input().split())

print(origin[n1-1:n2])
