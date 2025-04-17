import sys
input = sys.stdin.readline

# 대표자를 찾는 함수
# + 경로단축
def find(x):
    if x == lst[x]:
        return x
    
    # 경로 단축
    lst[x] = find(lst[x])
    return lst[x]

# Union 함수
def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:
        return
    
    # 대표자가 지민이 인경우 대표자는 무조건 지민이인걸로
    # 아니라면 작은쪽이 대표표
    if not ref_x or not ref_y:
        lst[ref_x] = 0
        lst[ref_y] = 0
    elif ref_x < ref_y:
        lst[ref_y] = ref_x
    else:
        lst[ref_x] = ref_y
    
N, M = map(int, input().split())
t = list(map(int, input().split()))
# 0번째는 지민 그 후로 사람의 번호 순서대로
lst = [i for i in range(N+1)]
party = [list(map(int, input().split())) for _ in range(M)]

# 만약 진실을 아는 사람이 없다면 파티의 숫자만큼 거짓말 할 수 있음
if t == [0]:
    print(M)
else:
    # 진실을 아는 사람들 끼리 같은 집합으로 묶음
    for i in range(1, t[0] + 1):
        union(0, t[i])

    # 파티들을 돌면서 같은 파티에 있는 사람들이라면 모두 같은 집합을 묶음
    for i in range(M):
        for j in range(2, party[i][0] + 1):
            union(party[i][1], party[i][j])
    # 지금까지의 상황
    # 같은 파티에 있는 사람이라면 모두 같은 집합에 있고
    # 같은 파티에 진실을 아는 사람이 한명이라도 있으면 모두 대표자가 지민이로 되어있음음
    cnt = 0

    # 파티를 돌면서 진실을 아는 사람이 있다면 break
    # 없다면 거짓말을 할 수 있으므로 cnt += 1 
    for i in range(M):
        for j in range(1, party[i][0] + 1):
            if find(party[i][j]) == find(0):
                break
        else:
            cnt += 1
    print(cnt)