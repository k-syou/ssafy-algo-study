from collections import deque

a, b = map(int,input().split())
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]


route = [[] for _ in range(N+1)] # 0번 인덱스는 버릴 거라서 N+1개
for i in range(M):
    route[arr[i][0]].append(arr[i][1])
    route[arr[i][1]].append(arr[i][0])
print(route)
def bfs(a, b):

    q = deque()
    visited = [0] * (N + 1)

    visited[a] = 1 # 시작점 방문처리
    q.append((a,0)) # 시작점(a)와 카운팅(0) queue에 넣기

    while q:
        num, cnt = q.popleft() # 숫자, 횟수로 queue에 첫번째꺼 꺼내기
        print(q)
        print(num,cnt)
        if num == b: # 숫자가 b랑 같다면
            return cnt # 횟수 return
        else: # 숫자가 b랑 다르다면 이 숫자가 갈 수 있는 경로 탐색
            # route의 num번 리스트가 갈 수 있는 경로들을 담고 있으니 next_route에 담고 하나씩 확인해보기
            for next_route in route[num]:
                if visited[next_route] == 1: # next_route가 방문한 곳이라면 pass
                    continue
                else: # 방문한 곳이 아니라면
                    q.append((next_route, cnt + 1)) # next_route와 카운팅 하나 올려서 q에 넣기
                    visited[next_route] = 1 # next_route 방문 처리
    return -1   # 함수를 다 돌았는데도 치환이 불가능하다면 -1 출력
print(bfs(a,b))


