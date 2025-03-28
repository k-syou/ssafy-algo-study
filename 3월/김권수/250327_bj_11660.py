import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
# dp[i][j] = board의 (0, 0) ~ (i, j) 까지의 합
dp = [[0] * N for _ in range(N)]

# 구간합 배열 만들기
for y in range(N):
    for x in range(N):
        dp[y][x] += board[y][x]
        if y:
            dp[y][x] += dp[y - 1][x]
        if x:
            dp[y][x] += dp[y][x - 1]
        if y and x:
            dp[y][x] -= dp[y - 1][x - 1]


def cal(y1, x1, y2, x2):
    # 구간합 계산
    global dp
    result = dp[y2][x2]
    if x1:
        result -= dp[y2][x1 - 1]
    if y1:
        result -= dp[y1 - 1][x2]
    if x1 and y1:
        result += dp[y1 - 1][x1 - 1]
    return result


res = []
for _ in range(M):
    # dp가 인덱스 0 부터 시작 함
    # 하지만 입력값은 1부터 시작하므로 받아올때 1을 빼줌
    loc = map(lambda l: int(l) - 1, input().split())
    res.append(cal(*loc))

print(*res, sep="\n")
