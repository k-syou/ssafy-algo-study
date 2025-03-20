from collections import deque

def cal(A, K):
    q = deque([(A, 0)])
    visited = set()

    while q:
        current, cnt = q.popleft()

        if current == K:
            return cnt
        
        if current > K or current in visited:
            continue
        visited.add(current)
    
        q.append((current+1, cnt+1))
        q.append((current*2, cnt+1))

A, K = map(int, input().split())
result = cal(A, K)
print(result)