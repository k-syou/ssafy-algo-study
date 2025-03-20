from collections import deque

dy = [-1, 0, 1, 0, -1, -1, 1, 1]
dx = [0, -1, 0, 1, -1, 1, -1, 1]


def searching(island, y, x):
    q = deque()
    q.append((y, x))
    island[y][x] = 0
    while q:
        ty, tx = q.pop()
        for i in range(8):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if island[ny][nx] == 0:
                continue
            island[ny][nx] = 0
            q.appendleft((ny, nx))


res = []
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    island = [[*map(int, input().split())] for _ in range(h)]
    cnt = 0
    for y in range(h):
        for x in range(w):
            if island[y][x]:
                searching(island, y, x)
                cnt += 1
    res.append(cnt)
print(*res, sep="\n")
