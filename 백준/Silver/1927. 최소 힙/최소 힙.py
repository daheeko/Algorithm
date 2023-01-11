import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
for i in range(N):
    value = int(input())
    if value == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, value)
