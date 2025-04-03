"블로그 : https://kspsd.tistory.com/15"

N, M = map(int, input().split())
beads = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    beads[s][e] = 1

