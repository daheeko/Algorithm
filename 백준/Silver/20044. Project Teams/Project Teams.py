n = int(input())
data = list(map(int, input().split()))

data.sort()
d1 = data[:n]
d2 = data[n:]
d2.reverse()

arr = [0] * n

for i in range(n):
    arr[i] = d1[i] + d2[i]

print(min(arr))
