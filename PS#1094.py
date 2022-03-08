#https://www.acmicpc.net/problem/1094

def main(x: int):
    if 64 % x == 0:
        return 1
    A = [32, 32]
    while True:
        if sum(A[0:-1]) >= x:
            del A[-1]
        if sum(A) == x:
            break
        n = A[-1] // 2
        del A[-1]
        if n > 0:
            A += [n, n]
    return len(A)

print(main(int(input())))
