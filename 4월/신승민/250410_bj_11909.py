# import heapq, sys
# input = sys.stdin.readline

# def dijkstra(sr, sc):
#     hq = [(0, sr, sc)]
#     dist = [[float('inf')] * N for _ in range(N)]
#     dist[sr][sc] = 0
#     while hq:
#         w, r, c = heapq.heappop(hq)
        
#         if (r, c) == (N-1, N-1):
#             return dist[r][c]
        
#         if dist[r][c] < w:
#             continue

#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
            
#             if nr<0 or nc<0 or nr>=N or nc>=N:
#                 continue
            
#             new_w = 0
#             if maze[nr][nc] >= maze[r][c]:
#                 new_w += maze[nr][nc] - maze[r][c] + 1
            
#             if dist[nr][nc] > new_w + dist[r][c]:
#                 dist[nr][nc] = new_w + dist[r][c]
#                 heapq.heappush(hq, (dist[nr][nc], nr, nc))
#     return dist[N-1][N-1]
            
            

# dir = [[0, 1], [1, 0]]
# N = int(input())
# maze = [list(map(int, input().split())) for _ in range(N)]
# print(dijkstra(0, 0))

import sys
input = sys.stdin.readline

def dp():
    dp_matrix = [[float('inf')]*N for _ in range(N)]
    dp_matrix[0][0] = 0
    for r in range(1, N):
        dp_matrix[r][0] = dp_matrix[r-1][0] + max(0, maze[r][0] - maze[r-1][0] + 1)
        dp_matrix[0][r] = dp_matrix[0][r-1] + max(0, maze[0][r] - maze[0][r-1] + 1)

    for r in range(1, N):
        for c in range(1, N):
            top = dp_matrix[r-1][c] + max(0, maze[r][c] - maze[r-1][c] + 1)
            left = dp_matrix[r][c-1] + max(0, maze[r][c] - maze[r][c-1] + 1)
            dp_matrix[r][c] = min(top, left)
    return dp_matrix[N-1][N-1]

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
print(dp())