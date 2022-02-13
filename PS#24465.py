#https://www.acmicpc.net/problem/24465

last = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def Constellation(month: int, date: int):
    total = sum(last[:month - 1]) + date
    if total < 20: return '염소'
    elif total < 50: return '물병'
    elif total < 80: return '물고기'
    elif total < 110: return '양'
    elif total < 141: return '황소'
    elif total < 173: return '쌍둥이'
    elif total < 204: return '게'
    elif total < 235: return '사자'
    elif total < 266: return '처녀'
    elif total < 296: return '천칭'
    elif total < 327: return '전갈'
    elif total < 356: return '사수'
    else: return '염소'

aloha, answer = set(), list()

for _ in range(7):
    M, D = map(int, input().split())
    aloha.add(Constellation(M, D))

for _ in range(int(input())):
    M, D = map(int, input().split())
    if Constellation(M, D) not in aloha:
        answer.append([M, D])

if answer:
    for i, j in sorted(answer):
        print(i, j)
else:
    print('ALL FAILED')
