n = int(input())
dp = [[0] * 10 for _ in range(n+1)]  # [자릿수][끝에 오는 수]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 초기값
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = sum(dp[n]) % 1000000000
print(result)