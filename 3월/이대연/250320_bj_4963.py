from collections import deque

def bfs(r, c):
    global visited
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]

            # 배열을 벗어나거나 방문했으면 pass
            if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0:
                if arr[nr][nc] == 1:
                    q.append([nr, nc])
                    visited[nr][nc] = 1



dr = [0, 0, 1, -1, -1, 1, -1, 1]
dc = [1, -1, 0, 0, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0] * w for _ in range(h)]
        cnt = 0
        for r in range(h):
            for c in range(w):
                if arr[r][c] == 1 and visited[r][c] == 0:
                    startr, startc = r, c
                    bfs(startr, startc)
                    cnt += 1
    print(cnt)
