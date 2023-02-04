from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


# __main__
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)