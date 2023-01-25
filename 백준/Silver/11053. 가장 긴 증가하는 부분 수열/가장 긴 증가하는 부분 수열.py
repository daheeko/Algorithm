n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * 1001
for i in range(1, n+1):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))