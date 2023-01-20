n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.reverse()
cnt = 0

for c in arr:
    if c > k:
        continue
    else:
        cnt += (k // c)
        k %= c
        
print(cnt)