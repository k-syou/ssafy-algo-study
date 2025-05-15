def f(s):
    global res
    S = 0
    for i in range(s, N):
        S += nums[i]
        if S == M:
            res += 1
            break
        

N, M = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

for i in range(N):
    f(i)
print(res)
