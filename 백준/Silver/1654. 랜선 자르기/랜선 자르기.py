import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = sorted([int(input()) for _ in range(k)])

result = 0
start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)