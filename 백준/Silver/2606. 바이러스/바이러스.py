from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


visited = [0] * (n+1)
q = deque([1])
visited[1] = 1

while q:
    now = q.popleft()
    for node in graph[now]:
        if visited[node] == 0:
            q.append(node)
            visited[node] = 1

print(sum(visited) - 1)