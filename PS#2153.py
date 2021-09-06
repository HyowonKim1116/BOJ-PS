#https://www.acmicpc.net/problem/2153

from string import ascii_lowercase, ascii_uppercase

def solution(n):
    if n < 4:
        return 'It is a prime word.'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'It is not a prime word.'
    return 'It is a prime word.'

alphabet = list(ascii_lowercase) + list(ascii_uppercase)
result = 0
word = input()

for w in word:
    add = alphabet.index(w) + 1
    result += add

answer = solution(result)
print(answer)
