from collections import deque

def bfs(a, k, cnt):
    q = deque()
    q.append([a, cnt])
    while q:
        a, cnt = q.popleft()
        if a == k:
            return cnt

        if visited[a]:
            continue

        visited[a] = 1
        na1 = a + 1
        na2 = a * 2

        if 0 <= na1 <= k:
            q.append([na1, cnt + 1])
        if 0 <= na2 <= k:
            q.append([na2, cnt + 1])

    return cnt


A, K = map(int, input().split())
visited = [0] * K
ans = bfs(A, K, 0)
print(ans)
