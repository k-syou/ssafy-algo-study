from collections import deque

dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]


def find_land(r, c):
    
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            
            if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0:
                if arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break    
    arr = [[*map(int, input().split())] for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                find_land(i, j)
                cnt += 1
    print(cnt)


from sys import stdin
from collections import deque
input = stdin.readline 

dx = [1, -1, 0, 0, 1, -1, 1, -1] # 그래프의 탐색 방향
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    graph[y][x] = 0
    while que:
       a, b = que.pop()
       for i in range(8):
           ny = b + dy[i]
           nx = a + dx[i]
           if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 1: # 그래프의 탐색조건
               que.append((nx, ny))
               graph[ny][nx] = 0


result = []
while True:
    res = 0
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: # 해당지점이 땅인 경우만 탐색
                bfs(j, i)
                res += 1 # 땅인경우 결과값 +1
    result.append(res) # 결과 리스트에 추가

for i in result:
    print(i) # 결과 출력