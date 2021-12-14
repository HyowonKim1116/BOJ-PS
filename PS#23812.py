#https://www.acmicpc.net/problem/23812

def function1(n):
    for _ in range(n):
        print('@' * N, end='')
        print(' ' * N * 3, end='')
        print('@' * N)

def function2(n):
    for _ in range(n):
        print('@' * N * 5)

N = int(input())

function1(N)
function2(N)
function1(N)
function2(N)
function1(N)
