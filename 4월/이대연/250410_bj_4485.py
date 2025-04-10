import sys,heapq
input = sys.stdin.readline

dr, dc = (0,0,-1,1), (-1,1,0,0)

def zelda(startr, startc):
    global visited
    hq = []
    heapq.heappush (hq, (arr[startr][startc], startr, startc))
     
    while hq:
        roopi,r,c = heapq.heappop(hq) # 5 0 0
        if r == N-1 and c == N-1:
            return roopi
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc]:
                continue
            else:
                heapq.heappush(hq, (roopi + arr[nr][nc],nr,nc))           
 
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans =zelda(0,0)
    print(ans)
    
    