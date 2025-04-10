import sys, heapq
input = sys.stdin.readline

def daijkstra(start):
    hq = []
    heapq.heappush(hq, (0,start))
    distance[start] = 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for next_dist, next_node in graph[node]:
            sum_dist = dist + next_dist
            if sum_dist < distance[next_node]:
                distance[next_node] = sum_dist
                heapq.heappush(hq,(sum_dist, next_node))
  
V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('inf')] * (V+1)

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w,v)) # 가중치 때문에 거리 먼저 넣어줌
    
daijkstra(K)

for i in range(1,V+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])