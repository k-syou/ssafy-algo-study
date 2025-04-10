import heapq
N, D = map(int, input().split())
temp = []
max_v = D
min_v = 2**2025
for _ in range(N):
    s, e, w = map(int, input().split())
    temp.append((s, e, w))
    min_v = min(min_v, s)
    max_v = max(max_v, e)
near = [[(i+1, 1)] for i in range(D+1)]
for i in range(N):
    s, e, w = temp[i]
    if e > D: continue # 도착 지점보다 더 가면 패스
    if w >= e-s: continue # 그냥 가는 게 더 빠르면 넣지 말기 <- !!!
    near[s].append((e, w))
# print(near)

# start_node = 0
pq = [(0, 0)]
dists = [2**2025] * (D+1)
dists[0] = 0

while pq:
    dist, node = heapq.heappop(pq)

    if node == D: break
    if dists[node] < dist: # 더 빨리 올 수 있다면
        continue
    # print(node, dist)

    for next_node, next_weight in near[node]:
        if next_node > D: continue
        next_dist = dist + next_weight
        
        # print('now_node', node, 'next_node', next_node, len(dists))
        if dists[next_node] <= next_dist:
            continue

        dists[next_node] = next_dist # 갱신
        # print(next_node, dists[next_node])
        heapq.heappush(pq, (next_dist, next_node))
        

print(dists[D])

