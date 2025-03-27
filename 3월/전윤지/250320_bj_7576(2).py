# 토마토
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


# 토마토 옮기기 함수
def tomato_bfs():
    day = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nr, nc = x + dr[i], y + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and (tomato[nr][nc] == 0):
                tomato[nr][nc] = tomato[x][y] + 1
                q.append([nr, nc])  # -1만나면 q에 안들어감감

    for t in tomato:
        for d in t:
            if d == 0:
                return -1

        day = max(day, max(t))
    return day - 1


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = deque()

# 토마토 박스에 토마토가 있으면 deque에 넣어
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1:
            q.append([n, m])

print(tomato_bfs())
# for t in tomato:
#     for d in t:
#         if d == 0:
#             print(-1)
#             # exit()

#     day = max(day, max(t))

# print(day - 1)
