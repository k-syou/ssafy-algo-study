# # # 4963. 섬의 개수 - DFS 사용
# # # 함수 선언
# # def DFS(sr, sc, R, C, visited):
    
# #     # 스택을 만든다. (크기를 특정할 수 없기 때문에 가장 크게 만든다.)
# #     stack = [0] * (R * C)
# #     top = 0

# #     # 스택에 시작하는 지점 (sr, sc)를 stack[top]에 넣는다.
# #     stack[top] = (sr, sc)

# #     # 스택이 빌 때까지 돌린다.
# #     while top != -1:

# #         # stack[top]의 요소(matrix의 좌표)를 r, c에 할당하고, top을 1 감소 시킨다.
# #         r, c = stack[top]
# #         top -= 1

# #         # 8방향을 순회한다.
# #         for dr, dc in dir:
# #             nr, nc = r + dr, c + dc

# #             if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and matrix[nr][nc]:  # nr, nc가 matrix안에 있고, 방문하지 않았으며 섬(matrix[nr][nc] == 1)이라면
# #                 visited[nr][nc] = True                                          # 방문표시를 하고
# #                 top += 1                                                        # top을 증가시키고
# #                 stack[top] = (nr, nc)                                           # nr, nc를 stack[top]에 넣는다.

# # # 순회 할 방향을 선언한다.
# # dir = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]

# # # 입력이 0, 0이 되기 전까지는 계속해서 테스트 케이스를 만족해야 함
# # while True:
    
# #     # input().split()을 통해서 너비(C), 높이(R)을 int로 입력받음
# #     C, R = map(int, input().split())
    
# #     # 입력이 0, 0이면 테스트를 종료 함
# #     if (R, C) == (0, 0):
# #         break
    
# #     # 섬의 정보를 matrix로 입력 받음
# #     matrix = list(list(map(int, input().split())) for _ in range(R))
    
# #     # matrix와 크기가 같은 visited와 결과 result를 만듬
# #     visited = [[False] * C for _ in range(R)]
# #     result = 0

# #     # matrix의 각 요소를 순회하면서 확인함
# #     for r in range(R):
# #         for c in range(C):

# #             if not visited[r][c] and matrix[r][c]:  # 방문하지 않았고 섬(matrix[r][c] == 1)이라면 
# #                 result += 1                         # 결과를 1 증가시키고
# #                 DFS(r, c, R, C, visited)            # DFS를 통해서 같은 섬을 다 방문한다.
    
# #     # 결과를 도출한다.
# #     print(result)


# # 4963. 섬의 개수 - BFS 사용
# # 함수 선언
# def BFS(sr, sc, R, C, visited):

#     # Queue를 만들고 front와 rear를 선언한다.
#     front, rear = -1, 0
#     q = [0] * (R * C + 1)

#     # Queue 시작하는 지점 (sr, sc)를 q[rear]에 넣는다.
#     q[rear] = (sr, sc)

#     # q가 빌 때까지 돌린다.
#     while front < rear:

#         # 데이터를 꺼내기 위해서 front를 1증가 시키고 r, c에 q[front]를 넣는다.
#         front += 1
#         r, c = q[front]

#         # 8방향을 순회안다.
#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
#             if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and matrix[nr][nc]:  # nr, nc가 matrix안에 있고, 방문하지 않았으며 섬(matrix[nr][nc] == 1)이라면
#                 rear += 1                                                       # 저장하기 위해서 rear를 증가시키고
#                 q[rear] = (nr, nc)                                              # nr, nc를 q[rear]에 넣는다.
#                 visited[nr][nc] = True                                          # 방문표시를 한다.

# # 순회 할 방향을 선언한다.
# dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]

# # 입력이 0, 0이 되기 전까지는 계속해서 테스트 케이스를 만족해야 함
# while True:

#     # input().split()을 통해서 너비(C), 높이(R)을 int로 입력받음
#     C, R = map(int, input().split())

#     # 입력이 0, 0이면 테스트를 종료 함
#     if (R, C) == (0, 0):
#         break

#     # 섬의 정보를 matrix로 입력 받음
#     matrix = list(list(map(int, input().split())) for _ in range(R))

#     # matrix와 크기가 같은 visited와 결과 result를 만듬
#     visited = [[False] * C for _ in range(R)]
#     result = 0

#     # matrix의 각 요소를 순회하면서 확인함
#     for r in range(R): 
#         for c in range(C):

#             if not visited[r][c] and matrix[r][c]:  # 방문하지 않았고 섬(matrix[r][c] == 1)이라면 
#                 result += 1                         # 결과를 1 증가시키고
#                 BFS(r, c, R, C, visited)            # DFS를 통해서 같은 섬을 다 방문한다.
    
#     # 결과를 도출한다.
#     print(result)
from pprint import pprint
def bfs(sr, sc):
    front, rear = -1, 0
    q = [0] * (R * C)
    q[rear]= (sr, sc)
    visited[sr][sc] = True

    while front < rear:
        front += 1
        r, c = q[front]

        for dr, dc in dir:
            nr, nc = r + dr, c + dc

            if nr<0 or nc<0 or nr>=R or nc>=C:
                continue
            if visited[nr][nc]:
                continue
            if matrix[nr][nc] == 0:
                continue
            visited[nr][nc] = True
            rear += 1
            q[rear] = (nr, nc)

res = []

dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
while True:
    C, R = map(int, input().split())
    if (C, R) == (0,0):
        break
    matrix = [list(map(int, input().split())) for _ in range(R)]
    num = 0
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 1 and visited[r][c] == False:
                num += 1
                bfs(r, c)
                # pprint(visited)
    res.append(num)

print(*res, sep='\n')
# print(res[0], res[1], res[2] ... res[-1])