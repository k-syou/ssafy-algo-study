import heapq, sys
input = sys.stdin.readline

N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]

dr, dc = (0, 1), (1, 0)

# hq = [(0, 0, 0, 0)]
# visited = [[0] * N for _ in range(N)]
# result = 0
# while hq:
#     cnt, dist, cr, cc = heapq.heappop(hq)
#     if (cr, cc) == (N-1, N-1):
#         result = cnt
#         break
#     if visited[cr][cc]:
#         continue
#     visited[cr][cc] = 1
#     for i in range(2):
#         nr = cr + dr[i]
#         nc = cc + dc[i]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         if visited[nr][nc]:
#             continue
#         n_cnt = cnt
#         if board[cr][cc] <= board[nr][nc]:
#             n_cnt += board[nr][nc] - board[cr][cc] + 1
#         heapq.heappush(hq, (n_cnt, dist - 1, nr, nc))

# print(result)
MAX = float('inf')
dp = [[MAX] * N for _ in range(N)]
dp[N-1][N-1] = 0
def dp_run(r, c):
    if dp[r][c] < MAX:
        return dp[r][c]
    
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nc >= N:
            continue
        v = 0
        if board[nr][nc] >= board[r][c]:
            v = board[nr][nc] - board[r][c] + 1
        dp[r][c] = min(dp[r][c], dp_run(nr, nc) + v)
    return dp[r][c]

dp_run(0, 0)
print(*dp, sep='\n')