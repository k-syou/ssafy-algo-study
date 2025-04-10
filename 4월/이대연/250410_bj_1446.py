import sys, heapq
input = sys.stdin.readline

def Dijkstra(start):
    hq = []
    heapq.heappush(hq, (0,start)) # 처음에는 거리 0으로 해서 heapque에 넣기
    distance[start] = 0 # 첫번째 노드의 거리는 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]: # heapque에서 꺼낸 거리가 내 거리보다 크다면 pass
            continue
        # 꺼낸 거리가 내 거리보다 작다면
        for next_dist, next_node in graph[node]:  # 내가 갈 수 있는 노드들과 거리를 순회
            sum_distance = dist + next_dist # 누적 거리는 나와 꺼낸 거리의 합
            if sum_distance < distance[next_node]: # 누적 거리가 내가 갈 수 있는 노드의 거리보다 작다면
                distance[next_node] = sum_distance # 바꿔주기
                heapq.heappush(hq,(sum_distance,next_node)) # 바꿔준 거리와 갈 수 있는 노드를 다시 heapque에 넣기

N, D = map(int,input().split())

graph = [[] for _ in range(D+1)] # 갈 수 있는 노드들의 정보를 담기 위한 리스트 생성
distance = [float("inf")] * (D+1) # 최종 거리 저장할 리스트

# 지름길이 없다면 거리가 1임을 알려주기 위해 저장
for i in range(D):
    graph[i].append((1,i+1)) # 거리 : 1로 고정, 갈 수 있는 노드 : 다음 숫자

    

for _ in range(N):
    start, end, fast_distance = map(int,input().split())

    # 구간의 끝지점이 최종목적지를 넘어서지 않고 # 지름길의 길이가 구간보다 작을 때만
    if end <=  D and (fast_distance < end-start):
        graph[start].append((fast_distance,end)) # 지름길, 다음에 갈 수 있는 구간

Dijkstra(0)
print(distance[D])