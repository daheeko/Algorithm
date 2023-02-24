import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
# trees.sort()

start, end = 0, max(trees)
result = []
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree >= mid:
            total += (tree - mid)
    if total >= m:
        result.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(result))