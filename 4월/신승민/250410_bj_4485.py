# import sys, heapq
# input = sys.stdin.readline


# def dijkstra(sr, sc, er, ec):
#     hq = [(matrix[sr][sc], sr, sc)]
#     visited = [[float('inf')] * N for _ in range(N)]
#     visited[sr][sc] = matrix[sr][sc]
#     while hq:
#         dist, r, c = heapq.heappop(hq)
        
#         for dr, dc in dir:
#             nr, nc = r + dr, c+ dc
#             if nr<0 or nc<0 or nr>=N or nc>=N:
#                 continue

#             new_d = visited[r][c] + matrix[nr][nc]
#             if visited[nr][nc] < new_d:
#                 continue
#             visited[nr][nc] = new_d
#             heapq.heappush(hq, (matrix[nr][nc], nr, nc))
#     return visited[er][ec]


# dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# while True:
#     i = 1
#     N = int(input())
#     if N == 0:
#         break
#     matrix = list(list(map(int, input().split())) for _ in range(N))
#     print(f'Problem {i}: {dijkstra(0, 0, N-1, N-1)}')
#     i += 1

import sys, heapq
input = sys.stdin.readline


def dijkstra(sr, sc, er, ec):
    hq = [(matrix[sr][sc], sr, sc)]
    visited = [[False] * N for _ in range(N)]

    while hq:
        dist, r, c = heapq.heappop(hq)
        
        if (r, c) == (er, ec):
            return dist

        if visited[r][c]:
            continue

        # dist로하면 시간초과
        visited[r][c] = True

        for dr, dc in dir:
            nr, nc = r + dr, c+ dc
            if nr<0 or nc<0 or nr>=N or nc>=N:
                continue

            if visited[nr][nc]:
                continue

            heapq.heappush(hq, (dist + matrix[nr][nc], nr, nc))


dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
i = 1
while True:
    N = int(input())
    if N == 0:
        break
    matrix = list(list(map(int, input().split())) for _ in range(N))
    print(f'Problem {i}: {dijkstra(0, 0, N-1, N-1)}')
    i += 1