from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

result = 0
visited = [False] * (n+1)

def bfs(start):
    global result
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                result += 1

bfs(1)
print(result)
