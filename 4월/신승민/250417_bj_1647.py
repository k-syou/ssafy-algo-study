import sys, heapq
input = sys.stdin.readline

# 대표자 찾는 함수
# + 경로 단축
def find(x):
    if x == ref[x]:
        return x
    ref[x] = find(ref[x])
    return ref[x]

# union 함수
def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:
        return
    
    if ref_x < ref_y:
        ref[ref_y] = ref_x
    else:
        ref[ref_x] = ref_y

# kuruscal이 맞는지 모르겠습니다...
def kuruscal():
    cnt = 0
    result = 0
    for s, e, d in edge:
        # 만약 현재 대표자가 같다면 트리 구조이므로 
        # s, e가 이어지면 cycle이 생기므로 continue
        if find(s) == find(e):
            continue
        # 두개의 대표자가 같지 않다면 두 집을 잇는 길을 잰다
        union(s, e)
        cnt += 1
        # 만약 길이 V-1개라면 모든 집이 이어진 것이므로 
        # result에 거리에 더하지 않고 return
        if cnt == V - 1:
            return result 
        result += d


V, E = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(E)]
ref = [i for i in range(V + 1)]
edge.sort(key= lambda x: x[2])

print(kuruscal())