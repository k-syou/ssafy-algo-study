# 시간 초과 -> union에 랭크 도입해서 해결
import sys
input = sys.stdin.readline

def find(x):
    # print(parents[x][0], x)
    while x != parents[x][0]:
        # print(parents[x][0])
        x = parents[x][0]
    return x
    # if parents[x] != x:
    # parents[x] = find(parents[x])
    # return parents[x]

def union(x, y, x_root, y_root):
    
    # 여기도 수정함 (랭크 삽입)
    if parents[x_root][1] < parents[y_root][1]:
        parents[x_root][0] = y_root
    elif parents[x_root][1] > parents[y_root][1]:
        parents[y_root][0] = x_root
    elif parents[x_root][1] == parents[y_root][1]:
        parents[x_root][1] += 1
        parents[y_root][0] = x_root

N, M = map(int, input().split()) # 점의 개수, 턴 수
parents = [[i, 0] for i in range(N)]

i = 1
result = 0
# j = False
for _ in range(M): 
    dot1, dot2 = map(int, input().split())
    
    x_root = find(dot1)
    y_root = find(dot2)
    
    if x_root == y_root:
        result = i
        break

    union(dot1, dot2, x_root, y_root)
    i += 1

print(result)