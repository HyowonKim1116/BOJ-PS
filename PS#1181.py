#https://www.acmicpc.net/problem/1181

word = {input() for _ in range(int(input()))}
result = sorted(list(word), key = lambda x: (len(x), x))
print('\n'.join(result))
