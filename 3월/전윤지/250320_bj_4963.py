"""1이고, 주변에 방문안한곳이 전부 0이어야함함"""

dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]


def dfs(x, y):
    visited[x][y] = 1

    if island[x][y] == 1:
        for i in range(8):
            nr = x + dr[i]
            nc = y + dc[i]

            if 0 <= nr < h and 0 <= nc < w:
                if island[nr][nc] == 1 and not visited[nr][nc] == 0:
                    dfs(nr, nc)


while True:
    w, h = map(int, input().split())
    # print(w, h)
    if w == 0 and h == 0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]
    # print(island)
    visited = [([0] * w) for _ in range(h)]
    # print(visited)
    cnt = 0

    for x in range(h):
        for y in range(w):
            if not visited[x][y] and island[x][y] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)
