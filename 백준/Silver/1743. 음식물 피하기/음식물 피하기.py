n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

def bfs(x, y):
    if graph[x][y] == 1:
        q = [(x, y)]
        cnt =  1
        while q:
            x, y = q.pop(0)
            visited[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny))
                        cnt += 1
                        graph[nx][ny] = cnt
                        visited[nx][ny] = True
for i in range(n):
    for j in range(m):
        bfs(i, j)

print(max(map(max, graph)))