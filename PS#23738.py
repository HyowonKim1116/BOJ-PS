#https://www.acmicpc.net/problem/23738

dictionary = {
    'A': 'a', 'B': 'v', 'E': 'ye', 'K': 'k',
    'M': 'm', 'H': 'n', 'O': 'o', 'P': 'r',
    'C': 's', 'T': 't', 'Y': 'u', 'X': 'h'
}

alphabet = input()

for alpha in alphabet:
    print(dictionary[alpha], end='')
