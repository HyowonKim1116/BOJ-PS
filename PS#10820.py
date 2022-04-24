#https://www.acmicpc.net/problem/10820

result = []

while True:
    try:
        string = input()
        lower, upper, number, blank = 0, 0, 0, 0
        for s in string:
            if s == ' ':
                blank += 1
            elif s.isdigit():
                number += 1
            elif s.isupper():
                upper += 1
            else:
                lower += 1
        result.append(f'{lower} {upper} {number} {blank}')
    except EOFError:
        break

print('\n'.join(result))
