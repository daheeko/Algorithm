import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0

for k in range(n):
    find = arr[k]  # 좋은 수인지 확인할 값
    i, j = 0, n-1
    while i < j:
        if arr[i] + arr[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif arr[i] + arr[j] > find:
            j -= 1
        else:
            i += 1

print(result)