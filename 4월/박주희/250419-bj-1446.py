from collections import deque
import sys
input = sys.stdin.readline

N, D = map(int, input().split()) # 지름길 개수 N, 목적지 D
graph = [[] for _ in range(D+1)]    # 모든 정점 등록 (0번부터 D번까지)
visited = [-1] * (D+1)

# 지름길 등록
for _ in range(N):
    s, e, w = map(int, input().split())
    if e <= D:
        graph[s].append((e, w))

# 일반 길 등록
for i in range(D):
    graph[i].append((i+1, 1))

q = deque([0])  # 시작점 집어넣기
visited[0] = 0  # 시작점 방문처리
while q:
    v = q.popleft()

    for nv, nw in graph[v]:
        # 한번도 방문한 적이 없거나, 방문했더라도 지금 살펴보고 있는 값이 더 작다면, 최소값 갱신 + q에 넣어주기
        if visited[nv] == -1 or visited[v] + nw < visited[nv]:  
            visited[nv] = visited[v] + nw
            q.append(nv)

print(visited[D])