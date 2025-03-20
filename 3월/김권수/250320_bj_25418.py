from collections import deque

A, K = map(int, input().split())


def bfs(a, k):
    q = deque()
    visited = [0] * (k + 1)
    q.append((a, 0))
    while q:
        num, cnt = q.popleft()
        if num == k:
            return cnt
        if num + 1 <= K and not visited[num + 1]:
            visited[num + 1] = 1
            q.append((num + 1, cnt + 1))
        if num * 2 <= K and not visited[num * 2]:
            visited[num * 2] = 1
            q.append((num * 2, cnt + 1))


print(bfs(A, K))
