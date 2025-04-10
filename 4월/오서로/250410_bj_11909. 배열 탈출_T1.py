# 다익스트라 # 시간 초과
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# print(*arr, sep='\n')

dists = [[0] * (n+1)] + [[0] + [2**2025]*n for _ in range(n)]
# print(*dists, sep='\n')
pq = [(1, 1, 0)]
dists[1][1] = 0

while pq:
    r, c, dist = heapq.heappop(pq)
    
    if dist > dists[r][c]:
        continue

    if r == n and c == n:
        print(dist)
        break
    
    for dr, dc in [[0, 1], [1, 0]]:
        nr, nc = r+dr, c+dc
        if nr<1 or nr>=(n+1) or nc<1 or nc>=(n+1):
            continue

        if arr[r][c] > arr[nr][nc]:
            next_dist = dist
        else:
            next_dist = dist + (arr[nr][nc] - arr[r][c] + 1)
        
        if dists[nr][nc] <= next_dist:
            continue
        
        dists[nr][nc] = next_dist
        heapq.heappush(pq, (nr, nc, next_dist))
