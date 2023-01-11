import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack= deque()
size_stack = len(stack)

for i in range(N):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
        size_stack += 1
    elif command[0] == "pop":
        if size_stack == 0:
            print(-1)
        else: 
            print(stack.pop())
            size_stack -= 1
    elif command[0] == "size":
        print(size_stack)
    elif command[0] == "empty":
        if size_stack == 0:
            print(1)
        else: 
            print(0)
    elif command[0] == "top":
        if size_stack == 0:
            print(-1)
        else: 
            print(stack[-1])