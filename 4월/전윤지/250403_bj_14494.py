n, m = map(int, input().split())
table = [[1] * (m+1) for _ in range(n+1)]

table[1][1] = 1

for i in range(2, n+1):
        for j in range(2, m+1):
            table[i][j] = table[i][j-1] + table[i-1][j-1] + table[i-1][j]


print(table[n][m] % (int(1e9) + 7))