# BFS
from collections import deque

A, K = map(int, input().split())
visited = [0]*2000000

q = []
q.append(A)
visited[A] = 0

while q:
    x = q.pop(0)
    # print(x)
    # print(x, visited[x])

    if x == K:
        break

    if x < K:
        if not visited[x+1]:
            q.append(x+1)
            visited[x+1] = visited[x]+1
        if not visited[x * 2]:
            q.append(x*2)
            visited[x*2] = visited[x]+1

print(visited[x])
