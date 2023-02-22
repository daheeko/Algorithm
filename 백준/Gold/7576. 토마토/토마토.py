import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                    
bfs()

for i in graph:
    for tomato in i:
        if tomato == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)
        
