import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
stack = []
num = 1
result = ''
for i in range(n):
    now = a[i]
    while now >= num:
        stack.append(num)
        num += 1
        result += '+'
    if stack.pop() == now:
        result += '-'
    else:
        result = 'NO'
        break

if result == 'NO':
    print(result)
else:
    print('\n'.join(result))
