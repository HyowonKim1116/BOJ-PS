#https://www.acmicpc.net/problem/11655

lowercase = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
answer = ''

for i in input():
    if i in lowercase:
        j = lowercase[lowercase.index(i) + 13]
        answer += j
        continue
    if i in uppercase:
        j = uppercase[uppercase.index(i) + 13]
        answer += j
        continue
    answer += i

print(answer)
