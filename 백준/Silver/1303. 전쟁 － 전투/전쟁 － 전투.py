n, m = map(int, input().split())
graph = [[c for c in input()] for _ in range(m)]
w, b = 0, 0
cnt = 0

def dfs(x, y, team):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] == 'X':
        return False
    if graph[x][y] == team:
        graph[x][y] = 'X'
        cnt += 1
        dfs(x-1, y, team)
        dfs(x, y-1, team)
        dfs(x+1, y, team)
        dfs(x, y+1, team) 
        return True
    return False


for i in range(m):
    for j in range(n):
        cnt = 0
        team = graph[i][j]
        if dfs(i, j, team):
            if team == 'W':
                w += cnt ** 2
            elif team == 'B':
                b += cnt ** 2

print(w, b)