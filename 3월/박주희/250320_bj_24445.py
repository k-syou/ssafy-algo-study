import sys
# sys.stdin = open("input.txt", "r")
from collections import deque
input = sys.stdin.read().splitlines()

N, M, R = map(int, input[0].split())
graph = [[] for _ in range(N+1)]
for i in range(1, M+1):
    s, e = map(int, input[i].split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1):
    graph[i].sort(reverse=True)

q = deque([R])
visited = [0]*(N+1)
visited[R] = 1
cnt = 1
while q:
    v = q.popleft()
    for next_v in graph[v]:
        if not visited[next_v]:
            cnt += 1
            visited[next_v] = cnt
            q.append(next_v)

print(*visited[1:], sep='\n')