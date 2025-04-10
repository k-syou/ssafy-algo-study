from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def btk(bd, dp):
    global n
    q = deque()
    q.append((n - 1, n - 1, bd[n - 1][n - 1]))
    while q:
        ty, tx, v = q.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if v + bd[ny][nx] >= dp[ny][nx]:
                continue
            dp[ny][nx] = v + bd[ny][nx]
            q.append((ny, nx, dp[ny][nx]))
    return dp[0][0]


T = 1
while True:
    n = int(input())
    if n == 0:
        break
    bd = [list(map(int, input().split())) for _ in range(n)]
    dp = [[10**6] * n for _ in range(n)]
    dp[n - 1][n - 1] = bd[n - 1][n - 1]
    ans = btk(bd, dp)
    print(f"Problem {T}: {ans}")
    T += 1
