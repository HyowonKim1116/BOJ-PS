#https://www.acmicpc.net/problem/22966

test = dict()

for _ in range(int(input())):
    title, level = input().split()
    test[int(level)] = title

print(test[min(test.keys())])
