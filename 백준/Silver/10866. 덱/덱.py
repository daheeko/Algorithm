import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deq = deque()
size_deq = len(deq)

for i in range(N):
    commnand = ''
    value = 0
    arr = input().split()
    command = arr[0]
    if len(arr) == 2:
        value = arr[-1]
    if command == "push_front":
        deq.appendleft(value)
        size_deq += 1
    elif command == "push_back":
        deq.append(value)
        size_deq += 1
    elif command == "pop_front":
        if size_deq == 0:
            print(-1)
        else: 
            print(deq.popleft())
            size_deq -= 1
    elif command == "pop_back":
        if size_deq == 0:
            print(-1)
        else: 
            print(deq.pop())
            size_deq -= 1
    elif command == "size":
        print(size_deq)
    elif command == "empty":
        if size_deq == 0:
            print(1)
        else: 
            print(0)
    elif command == "front":
        if size_deq == 0:
            print(-1)
        else: 
            print(deq[0])
    elif command == "back":
        if size_deq == 0:
            print(-1)
        else: 
            print(deq[-1])
