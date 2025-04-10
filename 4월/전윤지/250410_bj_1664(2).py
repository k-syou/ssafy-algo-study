import heapq
import sys
input = sys.stdin.readline
INF = float("INF")

def Dijkstra(start):
    hq = []
    heapq.heappush(hq,(0, start))
    distance[start] = 0

    while hq:
        dist, node = heapq.heappop(hq)

        if dist > distance[node]:
            continue

        for l, next in graph[node]:
            min_val = l + dist
            if min_val < distance[next]:
                distance[next] = min_val
                heapq.heappush(hq,(min_val, next))
###################################################################
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((1, i+1)) #(거리, 정점노드)

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D and (e-s > d):
        graph[s].append((d, e))
print(graph)
print(f"distance는 {distance}")        

Dijkstra(0)
print(f"distance는 {distance}")     
print(distance[D])