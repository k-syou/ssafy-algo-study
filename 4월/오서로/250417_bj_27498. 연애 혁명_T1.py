# 유니언 파인드
# 최대힙
# 최소 신장 트리
# 왜 이렇게 풀리는지는 모르겠음 -> 문제가 이해가 안됨
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
    # print(love_weight, s1, s2)
    if find(s1) != find(s2):
        # print(f'{s1}과 {s2}의 부모가 다르다')
        union(s1, s2)
    else:
        # print(f'{s1}과 {s2}의 부모가 같다 => {love_weight}')
        result += love_weight

print(result)


"""
student_num, loveline_num = map(int, input().split())

parents = [0] + [i for i in range(1, student_num+1)]

already_lovers_check = [False] * (student_num+1)
lovelines = []
max_loveweight = 0
for _ in range(loveline_num):
    s1, s2, love_weight, already_lovers = map(int, input().split())
    
    if already_lovers:
        already_lovers_check[s1] = True
        already_lovers_check[s2] = True
        student_num -= 2 # 짝이 없는 학생 수 감소 
        # union(s1, s2)
    # if 
    else:
        max_loveweight += love_weight
        heapq.heappush(lovelines, (-love_weight, s1, s2))

for i in range(len(lovelines)):
    if student_num < 2:
        break
    love_weight, s1, s2 = heapq.heappop(lovelines)
    print(love_weight)
    love_weight = - love_weight
    if already_lovers_check[s1] or already_lovers_check[s2]: # 둘 중 하나라도 짝이 있다면
        
        continue
    union(s1, s2)
    max_loveweight -= love_weight
    already_lovers_check[s1] = True
    already_lovers_check[s2] = True
    student_num -= 2

print(max_loveweight) 

# (6, 1, 3) (5, 2, 3) (4, 1, 2) (3, 2, 4) (2, 3, 4) (1, 1, 4)
# 1 3 2 
# 4
"""
