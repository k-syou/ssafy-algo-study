import sys
input = sys.stdin.readline

N = int(input())
# arr = [[223] * (N+1)] + [[223] + list(map(int, input().split())) for _ in range(N)]
# dp = [[223] * (N+1)] + [[223] + [0]*(N) for _ in range(N)]
arr = [[int(1e9)] * (N+1)] + [[int(1e9)] + list(map(int, input().split())) for _ in range(N)]
dp = [[int(1e9)] * (N+1)] + [[int(1e9)] + [0]*(N) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, N+1):
        if r == c == 1:
            continue
        up_coins = dp[r-1][c]
        left_coins = dp[r][c-1]
        if arr[r][c] >= arr[r-1][c]:
            up_coins += (arr[r][c] - arr[r-1][c] + 1)
        if arr[r][c] >= arr[r][c-1]:
            left_coins += (arr[r][c] - arr[r][c-1] + 1)

        dp[r][c] = min(up_coins, left_coins)

print(*dp, sep='\n')
print(dp[N][N])