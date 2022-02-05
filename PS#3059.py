#https://www.acmicpc.net/problem/3059

from string import ascii_uppercase

word = [input() for _ in range(int(input()))]

for w in word:
    test, value = list(ascii_uppercase), 0
    for i in w:
        try:
            test.remove(i)
        except:
            pass
    for t in test:
        value += ord(t)
    print(value)
