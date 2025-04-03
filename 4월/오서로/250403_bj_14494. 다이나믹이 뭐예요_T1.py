
n, m = map(int, input().split()) # (n, m)

D = [[0]*(m+1) for _ in range(n+1)]
D[1][1] = 1

for i in range(1, n+1): # 순회하면서 DP 채우기
    for j in range(1, m+1):
        if i == 1 and j == 1: continue # 1, 1은 이미 기본값 채움
        D[i][j] = D[i-1][j] + D[i][j-1] + D[i-1][j-1] # 왼쪽, 위, 대각선 왼쪽 위 더한 값

# print(*D, sep='\n')
print(D[n][m] % 1000000007)
'''
3 2

1 1
1 3 
1 5
'''