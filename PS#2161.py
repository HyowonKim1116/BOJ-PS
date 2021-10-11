#https://www.acmicpc.net/problem/2161

card = [i+1 for i in range(int(input()))]

while True:
    print(card.pop(0), end=' ')

    if len(card) == 0:
        break
    
    card.append(card.pop(0))
