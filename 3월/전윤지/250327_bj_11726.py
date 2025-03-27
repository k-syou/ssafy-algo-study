'''
2XN 타일링
https://www.acmicpc.net/problem/11726
'''

'''T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    dp = [0] * 301
    dp[10] = 1
    dp[20] = 3
    dp[30] = 5

    for i in range(40, N + 1, 10):
        dp[i] = dp[i - 10] + 2 * dp[i - 20]

    print(f"#{tc} {dp[N]}")'''

N = int(input())

dp=[0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)