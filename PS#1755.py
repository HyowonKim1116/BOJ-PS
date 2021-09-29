#https://www.acmicpc.net/problem/1755

nums = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

N, M = map(int, input().split())
cnt = 0

word = {i: ' '.join([nums[j] for j in str(i)]) for i in range(N, M+1)}
keys = dict(sorted(word.items(), key=(lambda x: x[1]))).keys()

for k in keys:
    cnt += 1
    if cnt % 10:
        print(k, end=' ')
    else:
        print(k)
