import sys
from collections import deque

input = sys.stdin.readline

S, E = map(int, input().split())
N, M = map(int, input().split())
visited = [-1]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

found = False
visited[S] = 0
hq = deque([S])
while hq and not found:
    v = hq.popleft()

    for nv in graph[v]:
        if visited[nv] == -1:
            visited[nv] = visited[v] + 1
            if nv == E:
                found = True
                break
            else:
                hq.append(nv)

print(visited[E])