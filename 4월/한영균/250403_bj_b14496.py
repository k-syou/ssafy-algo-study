from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    while q:
        v, cnt = q.popleft()
        
        if v == b:
            return cnt
        for i in range(1, n+1):
            if adj[v][i] == 1 and visited[i] == 0:
                q.append((i, cnt+1))
                visited[i] = 1
    return -1   

a, b = map(int, input().split())
n, m = map(int, input().split())
adj = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

print(bfs(a))