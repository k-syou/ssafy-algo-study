# bfs

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    q = []
    visited = [[0]*w for _ in range(h)]
    cnt = 0

    for r in range(h):
        for c in range(w):
            # print(r, c)
            if arr[r][c] == 1 and visited[r][c] == 0:
                q.append((r, c))
                visited[r][c] = 1
                cnt += 1

                while q:
                    xr, xc = q.pop(0)

                    for dr, dc in [[0, -1], [-1, 0], [0, 1], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                        nr = xr + dr
                        nc = xc + dc

                        if nr < 0 or nr >= h or nc < 0 or nc >= w:
                            continue

                        if arr[nr][nc] == 0:
                            continue

                        if not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))

    print(cnt)

"""
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
0 0
"""