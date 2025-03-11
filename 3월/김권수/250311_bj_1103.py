# 1103 게임
'''
<input>
3 7
3942178
1234567
9123532
'''

import sys
sys.setrecursionlimit(10 ** 7)

def set_type(v):
    # 구멍인 경우에는 그대로 리턴하고 아닌 경우 int로 형변환 
    if v == 'H': return v
    return int(v)

# 입력 받기
N, M = map(int, input().split())
board = [[*map(set_type, input())] for _ in range(N)]

# 시작지점
sr, sc = 0, 0

# 방문기록
visited = [[0] * M for _ in range(N)]

# 방향
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 메모라이징(dp)
# 각 위치에 도착할 수 있는 경우의 수 중 최대 이동횟수를 저장
dp = [[0] * M for _ in range(N)]

# 깊이 우선 탐색(백트래킹)
def backtrack(r, c, visited):
    global N, M, board, dp
    
    # 가지치기
    if r < 0 or c < 0 or r >= N or c >= M:
        return 0  # 범위를 벗어난 경우
    if board[r][c] == "H":
        return 0  # 현재 위치가 구멍("H")인 경우
    if visited[r][c]:
        return -1  # 무한루프에 빠지는 경우
    if dp[r][c]: return dp[r][c]  # 이미 방문해서 기록을 남긴 경우
    
    # 현재 위치의 이동거리(v)
    v = board[r][c]
    result = 0
    visited[r][c] = 1  # 방문 체크
    # 4방향 검사
    for i in range(4):
        # 다음 위치
        nr = r + dr[i] * v
        nc = c + dc[i] * v
        
        # backtrack 재귀 호출
        temp = backtrack(nr, nc, visited)
        if temp == -1:
            return -1  # 무한 루프에 빠진 경우
        result = max(result, 1 + temp)
    visited[r][c] = 0  # 방문 해제
    
    # 메모라이징
    dp[r][c] = result
    return result

print(backtrack(sr, sc, visited))


# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline

# def set_type(v):
#     if v == 'H': return v
#     return int(v)

# # 입력 받기
# N, M = map(int, input().split())
# board = [[*max(set_type, input())] for _ in range(N)]

# # 시작지점
# sr, sc = 0, 0

# # 방문기록
# visited = [[0] * M for _ in range(N)]
# visited[sr][sc] = 1

# # 방향
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)

# # 메모라이징(dp)
# # 각 위치에 도착할 수 있는 경우의 수 중 최대 이동횟수를 저장
# dp = [[0] * M for _ in range(N)]

# # 깊이 우선 탐색(백트래킹)
# def backtrack(r, c, move, visited):
#     global N, M, board, dp, result
    
#     # result 값 갱신
#     result = max(result, move)
    
#     # 4방향 검사
#     for i in range(4):
#         # 다음 위치
#         nr = r + dr[i] * board[r][c]
#         nc = c + dc[i] * board[r][c]
        
#         # 조건 체크
#         if nr < 0 or nc < 0 or nr >= N or nc >= M:
#             continue  # 범위 초과
#         if board[nr][nc] == "H":
#             continue  # 구멍에 빠진 경우
#         if move < dp[nr][nc]:
#             continue  # 이전 최대값 보다 작은 경우
#         if visited[nr][nc]:
#             result = -1
#             return  # 순환하는 경우(무한으로 움직일 수 있는 경우)
        
#         # dp 갱신
#         dp[nr][nc] = move + 1
        
#         # backtrack 재귀 호출
#         visited[nr][nc] = 1  # 방문 체크
#         backtrack(nr, nc, move + 1, visited)
#         if result == -1:
#             return  # 순환하는 경우(무한으로 움직일 수 있는 경우)
#         visited[nr][nc] = 0  # 방문 해제
        
# result = 0

# backtrack(sr, sc, 1, visited)
# print(result)