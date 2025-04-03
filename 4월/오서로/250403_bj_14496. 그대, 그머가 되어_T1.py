from collections import deque

a, b = map(int, input().split()) # a -> b로 글자(숫자) 바꾸기
N, M = map(int, input().split()) # 총 글자 개수, 간선

can_switch = [[] for _ in range(N+1)] # 인접 리스트

for _ in range(M): 
    s, e = map(int, input().split())
    can_switch[s].append(e)
    can_switch[e].append(s) # 무방향 그래프

# print(can_switch) # [[], [3, 4], [3, 4], [1, 2], [1, 2]]

visited = [0] * (N+1)
q = deque()
q.append((a, 0))
visited[a] = 1

t = False # 현재 글자가 b 글자인가
result = -1 # 기본값 -1
while q and not t:

    if t: break # 위에서 살펴보기에 필요 없음

    now, cnt = q.popleft() # 현재 글자, 교환 횟수

    if now == b: # b글자로 바뀌었다면
        t = True
        result = cnt # 교환 횟수 저장
        break

    for next in can_switch[now]: # 바꿀 수 있는 글자 리스트
        if visited[next]:
            continue

        q.append((next, cnt+1))
        visited[next] = 1

print(result)







