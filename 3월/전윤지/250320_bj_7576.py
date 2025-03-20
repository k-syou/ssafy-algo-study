# 토마토
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


# 토마토 옮기기 함수
def tomato_bfs():

    while q:
        x, y = q.popleft()

        for i in range(4):
            nr, nc = x + dr[i], y + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and (tomato[nr][nc] == 0):
                tomato[nr][nc] = tomato[x][y] + 1
                q.append([nr, nc])


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = deque()
day = 0

# 토마토 박스에 토마토가 있으면 deque에 넣어
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1:
            q.append([n, m])

tomato_bfs()
for t in tomato:
    for d in t:
        if d == 0:
            print(-1)

    day = max(day, max(t))

print(day - 1)

"""
1 -1 0 0 0 0
2 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

q = [(0, 0, 1), (3, 5, 1)]

(0, 0)
q = [(3, 5, 1), (1, 0, 2)]

(3, 5)
q = [(1, 0, 2), (2, 5, 2)]

result = max(result, time)

...
1 9 7 6 5 4
2 9 6 5 4 3
3 4 5 6 9 2
4 5 6 0 9 1

----

 0-1 7 6 5 4
-1 7 6 5 4 2
 7 6 5 4 2 1
 6 5 4 2 1 1

"""


"""
queue = deque([])
dx, dy = []
day = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])
            
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x , dy[i] + y
            if 0 <= nx < N and 0 <= ny and tomato[nx][ny] == 0:
                tomato[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])
                
bfs()
for i in 토마토:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day - 1)

"""
