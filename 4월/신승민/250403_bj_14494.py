def dp():
    for r in range(1, R+1):
        for c in range(1, C+1):
            matrix[r][c] = matrix[r-1][c] + matrix[r][c-1] + matrix[r-1][c-1]
R, C = map(int, input().split())
matrix = [[0] * (C+1) for _ in range(R+1)]
matrix[0][0] = 1

dp()

print(matrix[R][C]%1000000007)