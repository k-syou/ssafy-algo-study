# import sys
# sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
prefix_sum = [[0]*(M+1) for _ in range(N+1)]
# print(prefix_sum)

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + arr[i-1][j-1] - prefix_sum[i-1][j-1]
# print(prefix_sum)
result = -400000001
for x1 in range(1, N+1):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                result = max(result, prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])
print(result)