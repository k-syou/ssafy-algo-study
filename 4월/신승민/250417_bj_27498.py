import sys
input = sys.stdin.readline


# 대표자를 찾는 함수
# + 경로단축
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

# kuruscal 아닙니다....
def kuruscal():
    global cnt, result
    
    # 포기하도록 만든 사랑 관계 애정도의 합의 최솟 값
    # -> 포기하지 않게 만든 사랑 관계 애정도의 합은 최댓 값
    while R:
        # 애정도가 가장 큰 것들을 먼저 이어준다!
        s, e, c = R.pop()
    
        if find(s) == find(e):
            result += c
            continue
        union(s, e)
        cnt += 1
        if cnt == N - 1:
            return 

# K각 관계를 이루지 않는다 -> 사이클이 생기면 안된다.
N, M = map(int, input().split())
ref = [i for i in range(N+1)]
cnt = 0
R = []
result = 0

# 성사된 사랑 관계만 미리 이어준다.
for _ in range(M):
    s, e, c, d = map(int, input().split())
    if d:
        union(s, e)
        cnt += 1
        continue
    R.append((s, e, c))
R.sort(key=lambda x : x[2])

kuruscal()
for a, b, c in R:
    result += c
print(result)