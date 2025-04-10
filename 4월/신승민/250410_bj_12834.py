import heapq, sys
input = sys.stdin.readline

def prim(start):
    result = 0
    hq = [(0, start)]
    visited = [False] * (V + 1)
    while hq:
        distance, s = heapq.heappop(hq)

        if visited[s]:
            continue
        
        if s == A or s == B:
            result += distance

        if visited[A] and visited[B]:
            return result
        
        visited[s] = True

        for d, e in adj_list[s]:
            new_d = distance + d
            if visited[e]:
                continue
            heapq.heappush(hq, (new_d, e))

    return result

N, V, E = map(int, input().split())
A, B = map(int, input().split())
house = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, d = map(int, input().split())
    adj_list[s].append((d, e))
    adj_list[e].append((d, s))

result = 0
for i in house:
    result += prim(i)
print(result)