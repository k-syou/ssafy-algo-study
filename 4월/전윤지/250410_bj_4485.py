"""
왜ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ???????????????????
"""
import sys
input = sys.stdin.readline
import heapq
INF = float("INF")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def Dijkstra():
    hq = []
    heapq.heappush(hq,(cave[0][0],0,0)) #가중치, 위치
    distance[0][0] = 0
    
    while hq:
        rupee, y, x = heapq.heappop(hq)

        for i in range(4):
            nr = y + dr[i]
            nc = x + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                min_val = rupee + cave[nr][nc]

                if min_val < distance[nr][nc]:
                    distance[nr][nc] = min_val
                    heapq.heappush(hq, (min_val,nr, nc))


i = 1

while True:
    N = int(input()) #동굴의크기
    if N == 0:
        break

    cave = [list(map(int, input().split()) for _ in range(N))]
    distance = [[INF] * N for _ in range(N)]

    Dijkstra()
    print(f"Problem {i}: {distance[N-1][N-1]}")
    i += 1