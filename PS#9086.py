#https://www.acmicpc.net/problem/9086

result = []

for _ in range(int(input())):
    string = input()
    result.append(string[0] + string[-1])

print('\n'.join(result))
