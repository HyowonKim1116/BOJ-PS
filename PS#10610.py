#https://www.acmicpc.net/problem/10610

number = list(map(int, input()))

try:
    number.remove(0)
    if sum(number) % 3 == 0:
        number.sort(reverse = True)
        string = map(str, number)
        print(''.join(string) + '0')
    else:
        print(-1)
except ValueError:
    print(-1)
