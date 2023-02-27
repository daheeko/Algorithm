import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * n
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def dfs(v):
    global cnt
    visited[v] = True
    result[v-1] = cnt
    cnt += 1
    for node in graph[v]:
        if not visited[node]:
            dfs(node)


dfs(r)
print("\n".join(map(str, result)))