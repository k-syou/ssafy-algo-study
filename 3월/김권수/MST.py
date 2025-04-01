# 유니온 파인드

N = 7
parent = [*range(N)]


def find(node):
    global parent
    p_node = parent[node]
    if p_node != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    global parent
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        parent[p_b] = p_a
        return True
    return False


# 크루스칼
import heapq
heap = []

arr = [(18, 5, 3), (21, 1, 2), (25, 2, 6), (31, 0, 2), (32, 0, 1), (34, 3, 4), (40, 5, 4), (46, 2, 4), (51, 0, 6), (51, 4, 6)]

for i in arr:
    heapq.heappush(heap, i)

# 연결한 간선의 개수가 N - 1개가 될때까지 반복
cnt = 0
tot = 0
while heap:
    weight, a, b = heapq.heappop(heap)
    if union(a, b):
        cnt += 1
        tot += weight
        if cnt == N - 1:
            break

print(tot)

adj = [[] for _ in range(N)]
for w, a, b in arr:
    adj[a].append((w, b))
    adj[b].append((w, a))

def prim():
    heap = []
    for w, v in adj[0]:
        heapq.heappush(heap, (w, v))
    visited = [0] * N
    visited[0] = 1
    tot = 0
    cnt = 0
    while heap:
        # a = 현재 노드 번호
        weight, a = heapq.heappop(heap)
        if visited[a]:
            continue
        visited[a] = 1
        tot += weight
        cnt += 1
        if cnt == N - 1:
            return tot
        for w, v in adj[a]:
            if visited[v]:
                continue
            heapq.heappush(heap, (w, v))


print(prim())