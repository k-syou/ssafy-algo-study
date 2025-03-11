# 28075_스파이

##
import sys
sys.stdin = open("input.txt","r")

N, M = map(int,input().split()) # N : 총 일수, M : 최소 기여도
work = [list(map(int,input().split())) for _ in range(2)]
visited = [[0] * 3 for _ in range(2)]

result = 0
for r in range(2):
    for c in range(3):
        score = work[r][c]

def dfs(day,score,prev):
    global result
    if day == N:
        if score >= M:
            result += 1
        return
    for i in range(2):
        for j in range(3):
            next_score = score
            if j == prev:
                next_score += work[i][j] / 2
            else:
                next_score += work[i][j]
            dfs(day+1, score, j)
dfs(0,0,-1)
print(result)