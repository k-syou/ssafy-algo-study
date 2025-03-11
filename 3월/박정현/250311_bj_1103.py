import sys
input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

def game(r, c):
    global result, visited
    if result == -1:
        return -1
    t = int(arr[r][c])
    if memo[r][c] == -1:
        for d in range(4):
            nr, nc = r+dr[d]*t, c+dc[d]*t

            if nr<0 or nr>=N or nc<0 or nc >=M or arr[nr][nc]=='H':
                continue # for 문, 이 방향 스킵

            if visited[nr][nc]:
                result = -1
                return -1
            visited[nr][nc] = visited[r][c]+1
            result = max(visited[nr][nc], result)
            game(nr, nc)
            if result == -1:
                return -1
            visited[nr][nc] = 0
    else:
        return memo[r][c]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = list(map(int, input().split()))
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
memo = [[-1]*M for _ in range(N)]
result = 1
visited[0][0] = 1
game(0, 0)
print(result)



# import sys
# # sys.stdin = open("input.txt", "r")
# 
# def game(r, c):
#     global result, visited
#     if result == -1:
#         return
#     t = int(arr[r][c])
#     for d in range(4):
#         nr, nc = r+dr[d]*t, c+dc[d]*t
# 
#         if nr<0 or nr>=N or nc<0 or nc >=M or arr[nr][nc]=='H':
#             continue # for 문, 이 방향 스킵
# 
#         if visited[nr][nc]:
#             result = -1
#             return
#         visited[nr][nc] = visited[r][c]+1
#         result = max(visited[nr][nc], result)
#         game(nr, nc)
#         if result == -1:
#             return
#         visited[nr][nc] = 0
# 
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# N, M = list(map(int, input().split()))
# arr = [list(input()) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# result = 1
# visited[0][0] = 1
# game(0, 0)
# print(result)



# import sys
# sys.stdin = open("input.txt", "r")
#
# from collections import deque
#
# def game():
#     q = deque()
#     q.append([0, 0])
#     visited[0][0] = 1
#     result = visited[0][0]
#     while q:
#         r, c = q.pop()
#         if arr[r][c].isdecimal():
#             temp = int(arr[r][c])
#             for d in range(4):
#                 nr, nc = r+dr[d]*temp, c+dc[d]*temp
#
#                 if nr<0 or nr>=N or nc<0 or nc >=M or arr[nr][nc]=='H':
#                     continue # for 문, 이 방향 스킵
#
#                 if visited[nr][nc]:
#                     return -1
#                 q.append([nr, nc])
#                 visited[nr][nc] = visited[r][c]+1
#                 result = max(visited[nr][nc], result)
#     return result
#
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# N, M = list(map(int, input().split()))
# arr = [list(input()) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# print(game())
