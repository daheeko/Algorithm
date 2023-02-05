n, m = map(int, input().split())
graph = [[c for c in input()] for _ in range(m)]

cnt_w = []
cnt_b = []
w = 0
b = 0

def dfs_w(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y] == 'W':
        graph[x][y] = 'X'
        cnt_w.append(1)  # 
        dfs_w(x-1, y)
        dfs_w(x, y-1)
        dfs_w(x+1, y)
        dfs_w(x, y+1) 
        return True
    return False


def dfs_b(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y] == 'B':
        graph[x][y] = 'X'
        cnt_b.append(1)  # 
        dfs_b(x-1, y)
        dfs_b(x, y-1)
        dfs_b(x+1, y)
        dfs_b(x, y+1) 
        return True
    return False


for i in range(m):
    for j in range(n):
        if dfs_w(i, j):
            w += sum(cnt_w) ** 2
            cnt_w = []
        elif dfs_b(i, j):
            b += sum(cnt_b) ** 2
            cnt_b = []

print(w, b)

