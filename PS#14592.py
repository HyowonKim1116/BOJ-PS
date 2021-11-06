#https://www.acmicpc.net/problem/14592

def main(target: list, item: int):
    idx = []
    while True:
        try:
            idx.append(target.index(item))
            target[idx[-1]] = -1
        except ValueError:
            return idx

score, count, time = [], [], []

for _ in range(int(input())):
    s, c, t = map(int, input().split())
    score.append(s)
    count.append(c)
    time.append(t)

s_idx = main(score, max(score))

if len(s_idx) == 1:
    print(s_idx[0] + 1)
else:
    cnt = [count[i] for i in s_idx]
    c_idx = main(cnt, min(cnt))
    
    if len(c_idx) == 1:
        print(c_idx[0] + 1)
    else:
        tm = [time[i] for i in c_idx]
        print(tm.index(min(tm)) + 1)
