import sys
input = sys.stdin.readline

# 대표자 찾는 함수
# + 경로 단축
def find(x):
    if x == ref[x]:
        return x
    ref[x]= find(ref[x])
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


N, M = map(int, input().split())
ref = [i for i in range(N)]
lst = [tuple(map(int, input().split())) for _ in range(M)]
result = 0


for a, b in lst:
    result += 1
    # 현재 a, b의 대표자가 같다면
    # a, b를 잇는 길을 새로 만들게 된다면 
    # 사이클이 생기므로 break
    if find(a) == find(b):
        break
    if M == result and find(a) != find(b):
        result = 0
        break
    union(a, b)

print(result)