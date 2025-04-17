# 유니언 파인드
# 최대힙
# 최소 신장 트리
# 추측 : 삼각관계가 있다 = 사이클이 생긴다?

import heapq, sys
input = sys.stdin.readline

def find(x):
    while x != parents[x]:
        x = parents[x]
    return x

def union(x, y):
    X = find(x)
    Y = find(y)

    if X == Y: # 어차피 동일한 두 학생 간 사랑 관계는 여러 번 주어지지 않기에 불필요할 수 있음
        return
    
    if X > Y:
        parents[X] = Y
    else:
        parents[Y] = X    


student_num, loveline_num = map(int, input().split())

parents = [0] + [i for i in range(1, student_num+1)]

already_lovers_check = [False] * (student_num+1)
lovelines = []
max_loveweight = 0
for _ in range(loveline_num):
    s1, s2, love_weight, already_lovers = map(int, input().split())
    
    if already_lovers:
        union(s1, s2)
    else:
        max_loveweight += love_weight
        heapq.heappush(lovelines, (-love_weight, s1, s2))

result = 0
for _ in range(len(lovelines)):
    love_weight, s1, s2 = heapq.heappop(lovelines)
    love_weight = -love_weight

    if find(s1) != find(s2):
        union(s1, s2)
    else:
        result += love_weight

print(result)