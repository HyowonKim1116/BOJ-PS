#https://www.acmicpc.net/problem/10870

def main(n):
    if n < 2:
        return n
    return main(n - 1) + main(n - 2)

print(main(int(input())))
