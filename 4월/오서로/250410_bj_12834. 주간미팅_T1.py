# 다익스트라
import heapq
N, V, E = map(int, input().split()) # 팀원의 수, 장소의 수, 도로의 수
KIST, CRfood = map(int, input().split()) # 한 사람의 거리 di = (집-KIST의 최단 거리) + (집-씨알푸드의 최단 거리)

homes = list(map(int, input().split()))

edges = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2, w = map(int, input().split())
    edges[n1].append((n2, w))
    edges[n2].append((n1, w))

total = 0
for home in homes:
    # KIST 까지 찾기
    pq = [(0, home)]
    dists = [int(1e9)]*(V+1)
    dists[home] = 0 # !!

    to_KIST = -1
    to_CRfood = -1
    already_search_one = False
    while pq:
        now_dist, now_node = heapq.heappop(pq)
        
        if now_dist > dists[now_node]:
            continue

        if now_node == KIST:
            to_KIST = now_dist
            if already_search_one: break
            already_search_one = True
        
        if now_node == CRfood:
            to_CRfood = now_dist
            if already_search_one: break
            already_search_one = True
        
        for next_node, next_weight in edges[now_node]:
            next_dist = now_dist + next_weight

            if next_dist >= dists[next_node]:
                continue
            
            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    # if dists[KIST] > 10000*100+10: to_KIST = -1
    # if dists[CRfood] > 10000*100+10: to_CRfood = -1
    total += to_KIST + to_CRfood

print(total)