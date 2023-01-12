import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, ((abs(num), num)))