"""
14494 다이나믹이 뭐예요?

<문제요약>
→, ↓, ↘의 세 방향만 사용해서 한 번에 한 칸씩 이동할 때, 
왼쪽 위 (1, 1)에서 출발하여 오른쪽 아래 (n, m)에 도착하는 경우의 수 구하기

<입력>
n, m = 도착지 좌표

<출력>
(n, m 에 도착하는 경우의 수) % (10^9 + 7)

<알고리즘>
DP
"""
n, m = map(int, input().split())
MOD = 10**9+7

# 1, 1 에서 출발해서 n, m 과
# 0, 0 에서 출발해서 n-1, m-1은 같음
# dp[i][j] = i, j 위치에 도달할 수 있는 모든 경우의 수
dp = [[0] * m  for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        if i:
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
        if j:
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        if i and j:
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

print(dp[n-1][m-1] % MOD)
