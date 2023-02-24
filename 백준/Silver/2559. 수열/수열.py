import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

result = []
result.append(sum(temps[:k]))
idx = 0
while idx+k < n:
    result.append(result[idx] - temps[idx] + temps[idx+k])
    idx += 1
print(max(result))