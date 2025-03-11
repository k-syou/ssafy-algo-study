import sys
sys.setrecursionlimit(10**6)
# 런타임 에러
def dfs(r, c):
    global cnt
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr>=M or nc<0 or nc>=N:
            continue
        if nr == M-1 and nc == N-1: # 도착지점
            # print('도착')
            cnt += 1
            return
        if arr[nr][nc] >= arr[r][c]:
            continue
        dfs(nr, nc)
            
M, N = map(int, input().split()) # 세로의 크기 M
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
dfs(0, 0)
print(cnt)