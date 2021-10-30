#https://www.acmicpc.net/problem/4447

name = [input() for _ in range(int(input()))]

for n in name:
    g_count = n.lower().count('g')
    b_count = n.lower().count('b')
    
    if g_count > b_count:
        print(f'{n} is GOOD')
    elif g_count < b_count:
        print(f'{n} is A BADDY')
    else:
        print(f'{n} is NEUTRAL')
