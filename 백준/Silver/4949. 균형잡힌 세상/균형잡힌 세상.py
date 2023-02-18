import sys
input = sys.stdin.readline

open = ["(", "["]
close = [")", "]"]
while True:
    str = input().rstrip()
    if str == ".":
        break
    stack = []
    for c in str:
        if c in open:
            stack.append(c)
        elif c in close:
            if stack:
                top = stack.pop()
            else:
                stack.append(c)
                break
            if c == ")" and top  == "(":
                continue
            elif c == "]" and top == "[":
                continue
            else:
                stack.append(c)
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
