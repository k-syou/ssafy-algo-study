"""
<문제요약>
1 ~ N 번호가 붙은 구슬들의 무게 비교 정보를 알 수 있을 때,
무게가 중간이 될 수 없는 구슬의 개수를 구하세요

<입력>
N, M = 구슬의 개수, 비교해본 쌍의 개수
b1, b2 = b1 > b2, 즉 b1이 b2보다 무겁다(초과)

<알고리즘>
DFS
"""

N, M = map(int, input().split())
# 나보다 가벼운 구슬의 인접 행렬
l_adj = [[] for _ in range(N + 1)]
# 나보다 무거운 구슬의 인접 행렬
g_adj = [[] for _ in range(N + 1)]

# 인접 행렬 만들기
for _ in range(M):
    b1, b2 = map(int, input().split())
    l_adj[b1].append(b2)
    g_adj[b2].append(b1)


def dfs(adj, num, visited):
    # num 으로 부터 연결가능한 모든 정점의 개수 추출
    count = 0
    for nxt in adj[num]:
        if visited[nxt]:
            continue
        visited[nxt] = 1
        count += dfs(adj, nxt, visited) + 1
    return count


mid = (N - 1) // 2  # 중간 값
# 나보다 무겁거나, 가벼운 구슬의 개수가 중간 값을 넘어가면
# 절대로 무게가 중앙에 위치 할 수 없다.
res = 0
for num in range(1, N + 1):
    # 나보다 가벼운 구슬 개수 찾기
    visited = [0] * (N + 1)
    visited[num] = 1
    count = dfs(l_adj, num, visited)
    if count > mid:
        # 나보다 가벼운 구슬 개수가 mid 값 이상인 경우
        res += 1
        continue

    # 나보다 무거운 구슬 개수 찾기
    visited = [0] * (N + 1)
    visited[num] = 1
    count = dfs(g_adj, num, visited)
    if count > mid:
        # 나보다 무거운 구슬 개수가 mid 값 이상인 경우
        res += 1

print(res)
