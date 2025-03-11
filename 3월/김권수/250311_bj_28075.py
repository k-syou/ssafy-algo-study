N, M = map(int, input().split())
mission = [[*map(int, input().split())] for _ in range(2)]
result = 0


def dfs(cnt, total, before):
    global result
    if total >= M:
        result += 6 ** (N - cnt)
        return
    if cnt == N:
        return
    for i in range(2):
        for j in range(3):
            progress = mission[i][j]
            if j == before:
                progress /= 2
            dfs(cnt + 1, total + progress, j)


dfs(0, 0, -1)
print(result)