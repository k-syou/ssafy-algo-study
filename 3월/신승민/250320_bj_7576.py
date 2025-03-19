import sys
from collections import deque
input = sys.stdin.readline

def bfs():

    while q:
        r, c = q.popleft()
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if nr<0 or nc<0 or nr>=R or nc>=C:
                continue
            if visited[nr][nc] and visited[nr][nc] <= visited[r][c] + 1:
                continue
            if box[nr][nc] != 0:
                continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))
    return 

def fine_zero():
    global result
    m = 0

    for r in range(R):
        for c in range(C):
            if visited[r][c] == 0 and box[r][c] == 0:
                result = -1
                return
            if box[r][c] != -1:
                if m < visited[r][c]:
                    m = visited[r][c]
    result = m
    return

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
C, R = map(int, input().split())
q = deque()
box = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
result = 0
for r in range(R):
    for c in range(C):
        if box[r][c] == 1:
            q.append((r, c))
bfs()
fine_zero()

print(result)