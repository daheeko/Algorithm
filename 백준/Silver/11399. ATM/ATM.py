n = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
for i in range(n):
    total += ((n-i)*times[i])
print(total)