# 참고: https://velog.io/@dh1010a/Python-%EB%B0%B1%EC%A4%801520-%EB%82%B4%EB%A6%AC%EB%A7%89%EA%B8%B8

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 10억회라는 제한에 맞춰서 한계를 걸어줌.
# sys.stdin = open("input.txt", "r")

def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1
    if memo[r][c] == -1: # 가본적 없다면
        memo[r][c] = 0 # memo를 0으로 바꿈 (값 더하기 위해서)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<= nr <N and 0<=nc<M:
                if arr[nr][nc] < arr[r][c]:
                    memo[r][c] += dfs(nr, nc) # 재귀함수 dfs, memo[r][c] = memo[r][c] + dfs(nr, nc)
    return memo[r][c]


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[-1]*M for _ in range(N)] # memoization을 위한 2차원 배열
print(dfs(0, 0))


# def dfs(r, c):
#     global result
#     if r == N - 1 and c == M - 1:
#         result += 1
#         return
#     for i in range(4):
#         nr, nc = r+dr[i], c+dc[i]
#         if 0<= nr <N and 0<=nc<M:
#             if arr[nr][nc] < arr[r][c]:
#                 dfs(nr, nc)
#
#
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# result = 0
# dfs(0, 0)
# print(result)




# from collections import deque
#
# def bfs():
#     global result
#     q = deque()
#     q.append([0, 0])
#     while q:
#         r, c = q.popleft()
#         next_q = deque()
#         for i in range(4):
#             nr, nc = r+dr[i], c+dc[i]
#             if 0<= nr <N and 0<=nc<M:
#                 if arr[nr][nc] < arr[r][c]:
#                     next_q.append([nr, nc])
#                     q.append([nr, nc])
#         if len(next_q)!=0:
#             result += len(next_q)-1
#         print(q, next_q, result)
#
#
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# result = 1
# bfs()
# print(result)