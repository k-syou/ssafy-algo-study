# bfs
# 인접 리스트
import sys
# sys.stdin = open("./백준_SR/0320. 스터디/24445.input.txt", "r")
from collections import deque

input = sys.stdin.read
data = input().splitlines()
N, M, R = map(int, data[0].split()) # 정점 수, 간선 수, 시작 정점
links = [[] for _ in range(N+1)]

for i in range(1, M+1):
    u, v = map(int, data[i].split())
    links[u].append(v)
    links[v].append(u)
# print(links)

for link in links:
    link.sort(reverse=True)

# print(links)

result = [0] * (N+1)
q = deque([R])
cnt = 1
result[R] = cnt

while q:
    x = q.popleft()
    for node in links[x]:
        if not result[node]:
            # print(node, '추가')
            cnt += 1
            q.append(node)
            result[node] = cnt

sys.stdout.write("\n".join(map(str, result[1:])) + "\n")
