"""
https://kspsd.tistory.com/15
"""
import sys
input = sys.stdin.readline
# 모든 구슬들의 관계를 살펴보고 조건 확인하기

N, M = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]


for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1

# 플로이드 와샬
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1


ans = 0

for i in range(1, N+1):
    left_cnt = 0
    right_cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        elif arr[i][j] == 1: # 현재 구슬보다 가벼운 갯수 세기
            right_cnt += 1
        elif arr[j][i] == 1:# 현재 구슬 보다 무거운 갯수 세기
            left_cnt += 1
    if right_cnt > N//2 or left_cnt > N//2: # 가볍거나 무거운 개수가 중간값 보다 많으면 될 수가 없다
        ans += 1


print(ans)

# import sys
# sys.stdin = open('input.txt', 'r')
#
# N, M = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     son, par = map(int, input().split())
#     arr[par].append(son)
# print(arr)
# children = [0]*(N+1)
# parent = [0]*(N+1)
# visited = [0]*(N+1)
#
# for i in range(1, N+1):
#     if visited[i]:
#         continue
#     q = [i]
#     while q:
#         idx = q.pop()
#         visited[i]=1
#         if len(arr[idx])==0:
#             continue
#         for next in arr[idx]:
#             pass
