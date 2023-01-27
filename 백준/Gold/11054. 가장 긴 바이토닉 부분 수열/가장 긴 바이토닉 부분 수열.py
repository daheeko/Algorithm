n = int(input())
a = list(map(int, input().split()))
b = list(reversed(a))
d1 = [1] * 1001
d2 = [0] * 1001

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d1[i] = max(d1[i], d1[j]+1)

for i in range(n):
    for j in range(i):
        if b[i] > b[j]:
            d2[i] = max(d2[i], d2[j]+1)

result = [i + d for i, d in zip(d1, list(reversed(d2[:n])))]
print(max(result))