from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    heapq.heappush(adj[u], -v)
    heapq.heappush(adj[v], -u)


def bfs(adj, start):
    q = deque()
    q.append(start)
    result = [0] * N
    cnt = 1
    while q:
        num = q.popleft()
        if result[num - 1]:
            continue
        result[num - 1] = cnt
        cnt += 1
        while adj[num]:
            n = -heapq.heappop(adj[num])
            q.append(n)
    return result


print(*bfs(adj, R), sep='\n')
