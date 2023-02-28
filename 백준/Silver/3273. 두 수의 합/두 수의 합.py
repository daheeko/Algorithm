import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, len(arr) - 1
result = 0

while start < end:
    sum = arr[start] + arr[end]
    if sum <= x:
        start += 1
    elif sum > x:
        end -= 1
    if sum == x:
        result += 1

print(result)