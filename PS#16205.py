#https://www.acmicpc.net/problem/16205

number, name = input().split()
answer = [''] * 3

if number == '2':
    variable = ''
    for n in name.split('_'):
        variable += (n[0].upper() + n[1:])
    answer[0] = (variable[0].lower() + variable[1:])
    answer[1] = name
    answer[2] = variable
else:
    name = name[0].lower() + name[1:]
    variable = list(name)
    for i in range(len(name)):
        if i == 0:
            continue
        if name[i].isupper():
            variable[i] = '_' + name[i].lower()
    answer[0] = name
    answer[1] = ''.join(variable)
    answer[2] = (name[0].upper() + name[1:])

print('\n'.join(answer))
