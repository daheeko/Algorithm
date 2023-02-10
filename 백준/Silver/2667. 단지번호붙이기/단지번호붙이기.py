from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[int(c) for c in input().rstrip()] for _ in range(n)]
size = []
cnt = 1

def bfs(x, y):
    global cnt
    q = deque([(x, y)])
    graph[x][y] = cnt
    size.append(1)
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                size[cnt-2] += 1
                q.append((nx, ny))
                graph[nx][ny] = cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            bfs(i, j)

size.sort()       
print(len(size))
print('\n'.join(map(str, size)))
