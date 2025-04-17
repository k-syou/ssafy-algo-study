# 크루스칼로 풀기
# 최소 신장 트리
import heapq, sys
input = sys.stdin.readline

def find(x):
    while x != parents[x]:
        x = parents[x]
    return x

def union(price, x, y):
    global last, cnt
    X = find(x)
    Y = find(y)

    if X == Y:
        return 0
    
    if X > Y:
        parents[X] = Y
    else:
        parents[Y] = X
    # N -= 1

    last = price
    cnt += 1
    return price

house_num, load_num = map(int, input().split())
M = house_num - 1 # 최소 신장 트리 간선 수

parents = [0] + [i for i in range(1, house_num+1)]

edges = []
for _ in range(load_num):
    h1, h2, price = map(int, input().split())
    heapq.heappush(edges, (price, h1, h2))

min_cost = 0
last = 0
cnt = 0 # M과 비교할 변수
for _ in range(len(edges)):
    price, h1, h2 = heapq.heappop(edges)
    min_cost += union(price, h1, h2)
    if cnt == M:
        break
    
print(min_cost - last)
