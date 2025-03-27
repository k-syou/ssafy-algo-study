#반복문으로 풀어보기

n = int(input())
dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

# 재귀 함수로 풀어보기 (시간초과)

# def fibo(x):
#     global d
#     if x < 2:
#         d[x] = x
#         return d[x]
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# n = int(input())
# d = [0] * (n+1)

# fibo(n)
# print(d[n])



