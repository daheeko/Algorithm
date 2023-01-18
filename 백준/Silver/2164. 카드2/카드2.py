from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque([i for i in range(n, 0, -1)])

while True:
    if len(queue) == 1:
        break
    queue.pop()
    queue.appendleft(queue.pop())
    
print(queue.pop())