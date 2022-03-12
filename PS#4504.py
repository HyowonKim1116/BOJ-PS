#https://www.acmicpc.net/problem/4504

N = int(input())
number, answer = [], []

while True:
    A = int(input())
    if A == 0:
        break
    number.append(A)
    if A % N == 0:
        answer.append(True)
    else:
        answer.append(False)

for i in range(len(number)):
    if answer[i]:
        print(f'{number[i]} is a multiple of {N}.')
    else:
        print(f'{number[i]} is NOT a multiple of {N}.')
