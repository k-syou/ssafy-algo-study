from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def dfs(sr, sc, cnt):
    global is_infinite, total

    if is_infinite:
        return
    
    if visited[sr][sc]:
        is_infinite = True
        return
    
    visited[sr][sc] = 1
    step = board[sr][sc]
    total = max(total, cnt)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        nr = sr + dr[i]*step
        nc = sc + dc[i]*step
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'H':
            # if board[nr][nc] >= N and board[nr][nc] >= M:
            #     continue
            if board[nr][nc] == step:
                is_infinite = True
                return
            dfs(nr, nc, cnt+1)

    visited[sr][sc] = 0

N, M = [*map(int, input().split())]
board = [[int(c) if c.isdigit() else c for c in input()] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
is_infinite = False
total = 0

dfs(0, 0, 1)
print(-1 if is_infinite else total)


