'''
델타 사용해서 1인 경우 stack에 추가하기
실패!!!!!! ----------------------------------------------------------------
'''
# def count_island(W, H):
#     stack = []
#     cnt = 0
#     zero_cnt = 0
#     dr, dc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
#     for r in range(H):
#         for c in range(W):
#             if map_arr[r][c] == 1:
#                 for i in range(8):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if 0 <= nr < H and 0 <= nc < W and map_arr[nr][nc] == 1:
#                         if (nr, nc) not in stack:
#                             stack.append((nr, nc))
#                             if (r, c) not in stack:
#                                 stack.append((r, c))
#                                 cnt += 1
#                     else:
#                         zero_cnt += 1
#                 if zero_cnt == 8:
#                     cnt += 1
#                 zero_cnt = 0
                      
#     return cnt


# W, H = map(int, input().split())
# while W != 0 and H != 0:
#     map_arr = [[*map(int, input().split())] for _ in range(H)]
#     print(count_island(W, H))
    
#     W, H = map(int, input().split())

'''
visited, bfs 사용하기 ----------------------------------------------------------------
'''
from collections import deque


dr, dc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
W, H = map(int, input().split())
while W != 0 and H != 0:
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    arr = [[*map(int, input().split())] for _ in range(H)]
    for r in range(H):
        for c in range(W):
            no_way = False
            q = deque()
            if visited[r][c]:
                continue
            if arr[r][c] == 0:
                continue
            q.append((r, c))
            visited[r][c] = 1
            cnt += 1

            while q:
                sr, sc = q.popleft()
                for i in range(8):
                    nr = sr + dr[i]
                    nc = sc + dc[i]
                    if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and arr[nr][nc] == 1:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        
    print(cnt)
    W, H = map(int, input().split())