import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n, loc = map(int, input().rstrip().split())
    pr = deque(list(map(int, input().rstrip().split())))
    idx = deque([i for i in range(len(pr))])
    m = max(pr)
    cnt = 0
    while loc in idx:
        now = pr.popleft()
        if len(pr) == 0:
            cnt += 1
            break
        if now >= m:
            idx.popleft()
            cnt += 1
            m = max(pr)
        else:
            pr.append(now)
            idx.rotate(-1)
    print(cnt)


