# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append([i, j])

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    result = 0
    while q:
        i, j = q.popleft()
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                result = max(arr[ni][nj]-1, result)
                q.append([ni, nj])
                
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    return result


M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
