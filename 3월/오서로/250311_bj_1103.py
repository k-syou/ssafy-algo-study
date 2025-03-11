from collections import deque
from copy import deepcopy

def dfs(visited1, q1, N, M, r, c, round):
    k = int(board[r][c]) # 해당 위치에서 주변 둘러보기
    # print(r, c)
    global inf
    t = False

    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr = r + dr*k
        nc = c + dc*k

        now_visited = [visited1[r][:] for r in range(len(visited1))]
        now_q = deepcopy(q1)
        
        # print('nr, nc', nr, nc)
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue # 못감
        
        if board[nr][nc] == 'H': # 경계 안에는 있지만 구멍이면
            continue
        
        if now_visited[nr][nc] == 1: # 이전에 방문한 적 있으면
            inf = True
            return -1

        # 도착할 수 있으면
        now_q.append([nr, nc, round+1])
        now_visited[nr][nc] = 1
        t = True
        result = dfs(now_visited, now_q, N, M, nr, nc, round+1)
    
    if t == False:
        s_list.append(round)

N, M = map(int, input().split()) # 세로, 가로
board = [list(input()) for _ in range(N)]

round_list = []
r, c = 0, 0

q = deque()
visited = [[0]*M for _ in range(N)]

visited[r][c] = 1
q.append([r, c, 1])
inf = False # 무한대?
s_list = []
round = dfs(visited, q, N, M, 0, 0, 1)

result = max(s_list)

if inf == True:
    result = -1

print(result)
