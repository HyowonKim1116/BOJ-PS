#https://www.acmicpc.net/problem/4659

vowel = {'a', 'e', 'i', 'o', 'u'}
password, accept = [], []

def continue3(word: str):
    v, c = 0, 0
    for w in word:
        if w in vowel:
            v += 1
            c = 0
        else:
            c += 1
            v = 0
        if (v == 3) or (c == 3):
            return 0
    return 1

def same2(word: str):
    i = ''
    for w in word:
        if i != w:
            i = w
        elif i not in ['e', 'o']:
            return 0
    return 1

while True:
    word = input()
    if word == 'end':
        break
    password.append(word)

    if len(set(word)) == len(set(word) - vowel):
        result = False
    elif continue3(word) == 0:
        result = False
    elif same2(word) == 0:
        result = False
    else:
        result = True
    accept.append(result)

for i in range(len(password)):
    print(f'<{password[i]}> is', end=' ')
    if accept[i]:
        print('acceptable.')
    else:
        print('not acceptable.')
