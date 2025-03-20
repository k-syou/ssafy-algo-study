from collections import deque

def bfs():
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 > nr or nr >= N or 0 > nc or nc >= M or tomato[nr][nc] != 0:
                continue
            else:
                tomato[nr][nc] = tomato[r][c] + 1
                q.append((nr, nc))


M, N = map(int, input().split())
tomato = [[*map(int, input().split())] for _ in range(N)]
q = deque()
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            q.append((r, c))
bfs()
have_badtomato = False
result = 0
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 0:
            result = -1
            have_badtomato = True
            break
        if tomato[r][c]-1 > result:
            result = tomato[r][c]-1
    if have_badtomato:
        break
print(result)