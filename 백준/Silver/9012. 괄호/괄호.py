import sys
input = sys.stdin.readline


def is_vps(ps):
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                result = "NO"
                return result
            stack.pop()
    if len(stack) != 0:
        result = "NO"
    else:
        result = "YES"
    return result
            
t = int(input())

for i in range(t):
    ps = input().rstrip()
    print(is_vps(ps))
