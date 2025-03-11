# from collections import deque

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs (sr, sc, er, ec):
    global cnt
    if (sr, sc) == (er, ec):
        cnt += 1
        return
    for dr, dc in dir:
        nr, nc = sr + dr, sc + dc
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if matrix[nr][nc] >= matrix[sr][sc]:
            continue
        dfs(nr, nc, er, ec)

# def bfs(sr, sc, er, ec):
#     global cnt
#     q = deque()
#     q.append((sr, sc))
    
#     while q:
#         r, c = q.popleft()

#         if (r, c) == (er, ec):
#             cnt += 1

#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
#             if nr<0 or nr>=R or nc<0 or nc>=C:
#                 continue
#             if matrix[nr][nc] >= matrix[r][c]:
#                 continue
#             q.append((nr, nc))


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# def dfs(sr, sc, er, ec):
#     global cnt
#     top = 0
#     stack = [0] * (R * C)
#     stack[top] = (sr, sc)
    
#     while top >= 0:
#         r, c = stack[top]
#         top -= 1

#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
#             if nr<0 or nr>=R or nc<0 or nc>=C:
#                 continue
#             if matrix[nr][nc] >= matrix[r][c]:
#                 continue
#             if (nr, nc) == (er, ec):
#                 cnt += 1
#                 continue
#             top += 1
#             stack[top] = (nr, nc)    

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
# matrix = list(sys.stdin.readlines().rstrip())
cnt = 0
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dfs(0, 0, R-1, C-1)
print(cnt)
