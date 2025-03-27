import sys
input = sys.stdin.readline

dir = [[0, -1], [-1, 0]]

def cum_sum():
    for i in range(1, N):
        matrix[0][i] += matrix[0][i-1]
        matrix[i][0] += matrix[i-1][0]
        
    for r in range(1, N):
        for c in range(1, N):
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                
                if nr<0 or nc<0 or nr>=N or nc>=N:
                    continue
                matrix[r][c]+= matrix[nr][nc]
            matrix[r][c] -= matrix[r-1][c-1]

def cal_sum(sr, sc, er, ec):
    result = matrix[er][ec]
    if sr:
        result -= matrix[sr-1][ec]
    if sc:
        result -= matrix[er][sc-1]
    if sr and sc:
        result += matrix[sr-1][sc-1]

    return result

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cum_sum()

for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    print(cal_sum(sr-1, sc-1, er-1, ec-1))
    