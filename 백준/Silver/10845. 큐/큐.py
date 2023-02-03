import sys

input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    cmd = input().rstrip()
    if cmd == 'pop':
        print(q.pop(0)) if q else print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0) if q else print(1)
    elif cmd == 'front':
        print(q[0]) if q else print(-1)
    elif cmd == 'back':
        print(q[-1]) if q else print(-1)
    else:
        q.append(cmd.split()[1])