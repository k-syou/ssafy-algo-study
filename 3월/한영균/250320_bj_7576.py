# # from collections import deque

# # dr = [-1, 1, 0, 0]
# # dc = [0, 0, -1, 1]

# # def bfs():
# #     while q:
# #         r, c = q.popleft()
# #         for d in range(4):
# #             nr, nc = r + dr[d], c + dc[d]
# #             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
# #                 arr[nr][nc] = arr[r][c] + 1
# #                 q.append((nr, nc))

# # M, N = map(int, input().split())
# # arr = [list(map(int, input().split())) for _ in range(N)]
# # q = deque()

# # # BFS 시작점(익은 토마토) 추가
# # for i in range(N):
# #     for j in range(M):
# #         if arr[i][j] == 1:
# #             q.append((i, j))

# # bfs()

# # # 결과 확인
# # ans = 0
# # for i in range(N):
# #     for j in range(M):
# #         if arr[i][j] == 0:  # 익지 않은 토마토가 있으면 -1 출력 후 종료
# #             print(-1)
# #             exit()
# #         ans = max(ans, arr[i][j])

# # print(ans - 1)  # 시작이 1이므로 최종 일수는 -1 해야 함


# from collections import deque

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# def bfs():
#     while q:
#         r, c = q.popleft()
#         for d in range(4):
#             nr, nc = r + dr[d], c + dc[d]
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
#                 arr[nr][nc] = arr[r][c] + 1
#                 q.append((nr, nc))

# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# q = deque()

# # BFS 시작점(익은 토마토) 추가
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             q.append((i, j))

# bfs()

# # 결과 확인
# ans = 0
# has_unripe = False  # 익지 않은 토마토가 있는지 체크

# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             has_unripe = True  # 익지 않은 토마토가 있음
#         ans = max(ans, arr[i][j])
# print(arr)
# # 결과 출력
# if has_unripe:
#     print(-1)
# else:
#     print(ans - 1)  # 시작이 1이므로 최종 일수는 -1 해야 함
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))

M, N = map(int, input().split())
arr = [[*map(int, input().split()) ]for _ in range(N)]
q = deque()
have_un = False
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
bfs()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            have_un = True
        ans = max(ans, arr[i][j])
if have_un:
    print(-1)
else:
    print(ans - 1)


