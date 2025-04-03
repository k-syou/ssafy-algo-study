# bfs로 양쪽으로 최단 거리 찾고 비교하자
# -> 통과
from collections import deque

def bfs(start, next): # 시작점, 살펴볼 배열
    path = []
    q = deque()
    q.append((start, 0)) # 시작점 인큐 # 사실 cnt 필요 없을 듯
    visited = [0] * (N+1) 
    visited[start] = 1
    temp = 0 # 더 작은/큰 구슬 개수
    
    while q:
        now, cnt = q.popleft()
        path.append(now) 
        temp += 1 # 더 작은/큰 구슬 추가하기

        for n in next[now]: # 갈 수 있는 경로 찾기
            if visited[n]:
                continue
            visited[n] = 1
            q.append((n, cnt+1))
        
    return path, temp # 더 작은/큰 구슬들 번호 리스트(start 포함), 더 작은/큰 구슬 개수


N, M = map(int, input().split())
middle = N // 2 # 인덱스로 치면 N이 5일때, 2 -> 앞에 구슬이 2개까지 올 수 있다

next1 = [[] for _ in range(N+1)] 
next2 = [[] for _ in range(N+1)]

# 단방향 그래프
for _ in range(M): 
    light, heavy = map(int, input().split())
    next1[light].append(heavy) # idx보다 무거운 구슬 저장 # -> 자기보다 무거운 구슬들 찾기 위함
    # 예. 구슬 2번(idx)이 구슬 1번보다 무겁다
    next2[heavy].append(light) # idx보다 가벼운 구슬 저장

cannot = 0 # 중간에 올 수 없는 구슬의 총 개수
for i in range(1, N+1): # 첫 번째로 정렬할 구슬 선택

    a, temp1 = bfs(i, next1) # i에서부터 시작하자

    if temp1-1 > middle: # 만약 i보다 무거운운? 구슬이 middle(예.2개)가 넘는다면 
        cannot += 1
        continue # 다음 반복으로

    b, temp2 = bfs(i, next2) 

    if temp2-1 > middle: # 만약 i보다 가벼운? 구슬이 middle(예.2개)가 넘는다면 
        cannot += 1

print(cannot)
