#https://www.acmicpc.net/problem/9498

def main(score: int):
    if score < 60:
        return 'F'
    if score < 70:
        return 'D'
    if score < 80:
        return 'C'
    if score < 90:
        return 'B'
    return 'A'

print(main(int(input())))
