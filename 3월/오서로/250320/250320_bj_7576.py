# BFS로 풀기

from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def tomatoes(unripe, ripe):
    if not unripe:
        return 0

    while ripe and unripe > 0:
        # print('ripe', ripe, 'unripe', unripe)
        r, c, day = ripe.popleft()
        
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]

            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
                if container[nr][nc] == 0: # 익지 않은 토마토라면
                    unripe -= 1
                    visited[nr][nc] = 1
                    ripe.append((nr, nc, day+1))    

    if not unripe: # 다 익었으면
        return day
    else:
        return -1

M, N = map(int, input().split()) # 가로 칸 수, 세로 칸 수
container = [list(map(int, input().split())) for _ in range(N)]

unripe = 0 # 덜 익은 토마토의 개수
ripe = deque()
visited = [[0]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if container[r][c] == 0:
            unripe += 1
        elif container[r][c] == 1:
            ripe.append((r, c, 1)) # 익은 토마토의 좌표, 날짜는 0
            visited[r][c] = 1
# day = 0
result = tomatoes(unripe, ripe)
# print('ripe', ripe)
print(result)