import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

deq = deque([i+1 for i in range(N)])
result = []

while deq:
    for i in range(K-1):
        deq.append(deq.popleft())
    result.append(deq.popleft())

print("<"+", ".join(map(str, result))+">")