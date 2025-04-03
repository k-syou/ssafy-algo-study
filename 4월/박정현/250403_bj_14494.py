def fibo(N, M):
    for i in range(2, N+1):
        for j in range(2, M+1):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1]


n, m = map(int, input().split())
dp = [[1]*1001 for _ in range(1001)]
fibo(n, m)
print(dp[n][m] % 1000000007)
