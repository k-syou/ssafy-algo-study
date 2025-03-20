M, N = map(int, input().split())
box = [[*map(int, input().split())] for _ in range(N)]
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    from collections import deque
    q = deque()
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                q.append((r, c, 0))
    result = 0
    while q:
        tr, tc, days = q.popleft()
        result = days
        for i in range(4):
            nr = tr + dr[i]
            nc = tc + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if box[nr][nc] != 0:
                continue
            box[nr][nc] = 1
            q.append((nr, nc, days + 1))
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    return result

print(bfs())