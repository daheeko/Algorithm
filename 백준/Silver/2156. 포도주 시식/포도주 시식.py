n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * 10001

dp[0] = arr[0]   # n=1일 때 여기까지만
if n > 1:  # n=2일 때 여기까지만
    dp[1] = arr[0] + arr[1]
if n > 2:  # 그 이후는 가능
    dp[2] = max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])

print(dp[n-1])