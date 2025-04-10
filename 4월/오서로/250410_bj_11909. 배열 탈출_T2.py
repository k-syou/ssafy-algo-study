# DP 사용 # 통과
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(*arr, sep='\n')

dp = [[0]*n for _ in range(n)]

dp[0][0] = 0

for r in range(n):
    for c in range(n):
        if r == 0 and c == 0: continue
        candidate1, candidate2 = int(1e9), int(1e9) 
        # 2 **2025에서 int(1e9)로 바꾸니 시간 줄어듦
        if r-1 >= 0:
            candidate1 = dp[r-1][c]
            if arr[r][c] >= arr[r-1][c]:
                candidate1+= (arr[r][c] - arr[r-1][c] + 1)
        if c-1 >= 0:
            candidate2 = dp[r][c-1] 
            if arr[r][c] >= arr[r][c-1]:
                candidate2 += (arr[r][c] - arr[r][c-1] + 1)
        dp[r][c] = min(candidate1, candidate2)
    
# print(*dp, sep='\n')
print(dp[n-1][n-1])
"""
[0, 0, 3, 3]
[2, 2, 2, 3]
[2, 2, 4, 4]
[7, 3, 3, 3]

"""