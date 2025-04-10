# 다익스트라
import heapq
tc = 0
while True:
    tc += 1
    N = int(input()) # 동굴의 크기
    if N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]

    pq = [(0, 0, arr[0][0])]
    dists = [[int(1e9)]*N for _ in range(N)]
    dists[0][0] = arr[0][0]

    while pq:
        r, c, now_dist = heapq.heappop(pq)
        
        if r == N-1 and c == N-1:
            continue

        if now_dist > dists[r][c]:
            continue

        for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
            nr, nc = r+dr, c+dc

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue

            new_dist = now_dist + arr[nr][nc]

            if new_dist >= dists[nr][nc]:
                continue
            
            dists[nr][nc] = new_dist
            heapq.heappush(pq, (nr, nc, new_dist))
    
    print(f'Problem {tc}: {dists[N-1][N-1]}')

"""
# 다익스트라
import heapq
tc = 0
while True:
    tc += 1
    N = int(input()) # 동굴의 크기
    if N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]

    pq = [(arr[0][0], 0, 0)]
    dists = [[int(1e9)]*N for _ in range(N)]
    dists[0][0] = arr[0][0]

    while pq:
        now_dist, r, c = heapq.heappop(pq)
        
        if r == N-1 and c == N-1:
            continue

        if now_dist > dists[r][c]:
            continue

        for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
            nr, nc = r+dr, c+dc

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue

            new_dist = now_dist + arr[nr][nc]

            if new_dist >= dists[nr][nc]:
                continue
            
            dists[nr][nc] = new_dist
            heapq.heappush(pq, (new_dist, nr, nc))
    
    print(f'Problem {tc}: {dists[N-1][N-1]}')
    """