from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    continue
    return graph[n-1][m-1]

print(bfs(0, 0))