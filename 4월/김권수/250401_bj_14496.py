'''
<문제요약>
a -> b 로 바꾸기 위한 최소 변환횟수 구하기
간선이 따로 주어지며, 변경이 불가능한 경우 -1 출력

<입력>
a, b = 바꾸려고 하는 문자 a, b
N, M = 전체 문자의 개수, 문자 쌍(간선)의 개수
ni, mi = 간선 표현 (M개)

<알고리즘>
BFS
'''

import sys
from collections import deque

input = sys.stdin.readline
a, b = map(int, input().split())
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]  # 간선 행렬 만들기
for _ in range(M):
    x, y = map(int, input().split())
    # 양방향 그래프로 생성
    adj[x].append(y)
    adj[y].append(x)


def bfs(adj, a, b):
    q = deque([(0, a)])
    visited = [0] * (N + 1)
    visited[a] = 1
    while q:
        cnt, cur = q.popleft()
        if cur == b:
            return cnt
        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            q.append((cnt+1, nxt))
    return -1

print(bfs(adj, a, b))
