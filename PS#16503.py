#https://www.acmicpc.net/problem/16503

def change(O: str):
    if O == '/':
        return '//'
    return O

K1, O1, K2, O2, K3 = input().split()
O1, O2 = change(O1), change(O2)

x = eval(f'({K1}{O1}{K2}){O2}{K3}')
y = eval(f'{K1}{O1}({K2}{O2}{K3})')

if (O1 == '//') and (int(K1) * eval(f'{K2}{O2}{K3}') < 0):
    z = abs(eval(f'{K2}{O2}{K3}'))
    y = -eval(f'{abs(int(K1))}{O1}{z}')
if (O2 == '//') and (eval(f'{K1}{O1}{K2}') * int(K3) < 0):
    z = abs(eval(f'{K1}{O1}{K2}'))
    x = -eval(f'{z}{O2}{abs(int(K3))}')

print(f'{min(x, y)}\n{max(x, y)}')
