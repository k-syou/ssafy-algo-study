import sys
input = sys.stdin.readline

N, D = map(int, input().split())
dp = [i for i in range(D+1)]
short = []

for _ in range(N):
    s, e, d = map(int, input().split())
    if e - s > d:
        short.append((s, e, d))
short.sort()

for s, e, d in short:
    for i in range(1, D+1):
        if e == i:
            dp[i] = min(dp[i], dp[s]+d)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)

print(dp[D])