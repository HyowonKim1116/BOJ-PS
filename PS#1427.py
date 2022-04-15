#https://www.acmicpc.net/problem/1427

number = sorted(list(map(int, input())), reverse = True)

print(''.join(map(str, number)))
