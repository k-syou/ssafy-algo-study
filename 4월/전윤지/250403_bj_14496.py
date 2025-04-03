from collections import deque

def bfs(a, b):
    q = deque([a])
    visited[a] = 0

    #1. a랑 b가 같은문자라면?
    if a == b:
        return 0
    
    while q:
        node = q.popleft()

        for i in adj_list[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)

                if i == b:
                    return visited[i]
                
    return -1

a, b = map(int, input().split())
N, M = map(int, input().split())

adj_list = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [0] * (N+1)

print(bfs(a, b))