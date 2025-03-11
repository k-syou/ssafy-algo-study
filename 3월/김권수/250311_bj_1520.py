import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]

dp = [[-1] * M for _ in range(N)]
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def dfs(y, x):
    global dp
    if y == N - 1 and x == M - 1:
        return 1
    if dp[y][x] >= 0:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if board[y][x] <= board[ny][nx]:
            continue
        dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0, 0))