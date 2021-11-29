#https://www.acmicpc.net/problem/1076

color = [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white'
]

C1 = str(color.index(input()))
C2 = str(color.index(input()))
C3 = 10 ** (color.index(input()))

print(int(C1 + C2) * C3)
