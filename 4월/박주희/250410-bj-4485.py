import sys
input = sys.stdin.readline
import heapq

'''
최소값(INF)을 갱신하지 않고, visited 여부만 조건으로 처리하고 싶다면?
1. visited 에는 누적 값 저장 필요 (현재 노드까지의 누적 가중치 저장)
2. visited 처리는 heappop 시점에 처리해야 함
3. 그러기 위해서는 누적 가중치를 들고다니면서 q에 넣어주어야 함
'''
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
num = 0
while True:
    N = int(input())
    if N == 0:
        break
    num += 1
    
    cave = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    q = [(cave[0][0], 0, 0)]    # 가중치(도둑루피)의 누적합, r, c

    while q:
        w, sr, sc = heapq.heappop(q)

        if visited[sr][sc] != -1:   # 이미 방문한 적이 있다면 패스
            continue
        visited[sr][sc] = w         # 처음 방문한다면 최소값 확정 (pop 한 값에 담겨있는 w 가 최소값)

        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:  # 배열을 벗어나지 않는다면
                new_w = visited[sr][sc] + cave[nr][nc]  # 누적값 계산 후 (현재 노드까지의 누적값 + 다음 노드의 가중치)
                heapq.heappush(q, (new_w, nr, nc))      # 누적값을 q에 넣어주자.
    
    print(f'Problem {num}: {visited[N-1][N-1]}')
            
        
