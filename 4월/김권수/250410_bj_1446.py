# 지름길
import heapq

N, D = map(int, input().split())

shortcuts = {}
for _ in range(N):
    s, g, d = map(int, input().split())
    if s > D or g > D:
        continue
    if s in shortcuts:
        shortcuts[s].append((g, d))
    else:
        shortcuts[s] = [(g, d)]
# print(shortcuts)
next_loc = sorted(shortcuts.keys())
hq = [(0, 0)]
visited = [0] * (D + 1)
result = 0
while hq:
    dist, cur = heapq.heappop(hq)
    if cur == D:
        result = dist
        break
    if visited[cur]:
        continue
    # print(dist, cur)
    visited[cur] = 1
    for nxt, n_dist in shortcuts.get(cur, []):
        if visited[nxt]:
            continue
        heapq.heappush(hq, (dist+n_dist, nxt))
    heapq.heappush(hq, (dist+1, cur+1))
print(result)
