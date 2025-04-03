from collections import deque

def yamin():
    global a, b
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        # print(q, visited)
        idx = q.popleft()

        if idx == b:
            print(visited[idx]-1)
            return

        for num in arr[idx]:
            if visited[num]==0:
                visited[num] = visited[idx] + 1
                q.append(num)
    print(-1)

a, b = map(int, input().split())
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [1]+[0]*N
for _ in range(M):
    char1, char2 = map(int, input().split())
    arr[char1].append(char2)
    arr[char2].append(char1)
# print(arr, visited)
yamin()