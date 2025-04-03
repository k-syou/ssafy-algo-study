# import sys
# input = sys.stdin.readline

# def count(num):
#     front, rear = -1, 0
#     visited = [float('inf')] * (N + 1)
#     q= []
#     q.append(num)
#     visited[num] = 1
    
#     while front < rear:
#         front += 1
#         num = q[front]
        
#         for i in adj_list[num]:
#             if visited[i] < visited[num] + 1:
#                 continue
            
#             rear += 1
#             q.append(i)
#             visited[i] = visited[num] + 1
#     return visited[b]

    

# a, b = map(int, input().split())
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]

# for _ in range(M):
#     s, e = map(int, input().split())
#     adj_list[s].append(e)
#     adj_list[e].append(s)


# result = count(a)
# print(result-1)

from collections import deque
import sys
input = sys.stdin.readline

def count(s, e):
    q = deque()
    q.append((s,0))
    visited= [False] * (N+1)
    visited[s] = 1
    while q:
        num, cnt = q.popleft()
        
        if num == e:
            return cnt
        for i in adj_list[num]:
            if i == s:
                continue
            if visited[i]:
                continue
            q.append((i, cnt + 1))
            visited[i] = 1
    return -1
    

a, b = map(int, input().split())
N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)


result = count(a, b)
print(result)