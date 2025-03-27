'''
n = 1 -> 1가지
n = 2 -> 2가지
n = 3 -> 3가지
n = 4 -> 5가지
..
n이 1개 증가할 수록 경우의 수는 피보나치 수열과 똑같이 증가한다
'''
n = int(input())


dp = [0] * (n+1)
print(dp)
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])