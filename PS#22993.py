#https://www.acmicpc.net/problem/22993

def main(s: list):
    s1 = s.pop(0)
    s.sort()
    for i in s:
        if s1 <= i:
            return 'No'
        s1 += i
    return 'Yes'

N = int(input())
A = list(map(int, input().split()))

print(main(A))
