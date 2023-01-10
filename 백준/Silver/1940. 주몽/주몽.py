import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt, i, j = 0, 0, n-1

while i < j:
    if arr[i] + arr[j] < m:
        i += 1
    elif arr[i] + arr[j] > m:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1
print(cnt)
