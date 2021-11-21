#https://www.acmicpc.net/problem/4949

answer = []

while True:
    string = input()

    if string == '.':
        print('\n'.join(answer))
        break

    parentheses, flag = [], True

    for s in string:
        if s in ['(', '[']:
            parentheses.append(s)
        elif s in [')', ']']:
            try:
                item = parentheses.pop()
                if item + s not in ['()', '[]']:
                    flag = False
                    break
            except IndexError:
                flag = False
                break
    
    if flag and parentheses == []:
        answer.append('yes')
    else:
        answer.append('no')
