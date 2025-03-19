def bfs(r):
    cnt = 1
    front, rear = -1, 0
    visited = [False] * (N+1)
    visited[r] = True
    q = [0] * N
    q[rear] = r
    result[r] = cnt
    while front < rear:
        front += 1
        s = q[front]

        for i in adj_matrix[s]:
            if visited[i]:
                continue
            cnt += 1
            result[i] = cnt
            visited[i] = True
            rear += 1
            q[rear] = i

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
adj_matrix = [[] for _ in range(N+1)]
result = [0] * (N+1)

for s, e in edge:
    adj_matrix[s].append(e)
    adj_matrix[e].append(s)

for row in adj_matrix:
    row.sort(reverse=True)

bfs(R)

for i in range(1, N+1):
    print(result[i])