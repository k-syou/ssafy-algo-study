# 연산 1 : 정수 A에 1을 더한다
# 연산 2 : 정수 A에 2를 곱한다
import sys
sys.setrecursionlimit(10**9)
def make_number(A,K,cnt):
    global result, dp
    # 종료조건
    if A > K:
        return
    if dp[A] <= cnt:
        return
    else:
        dp[A] = cnt
    if A == K:
        result = min(cnt, result)
        return
    else:
        make_number(2*A, K, cnt+1)
        make_number(A+1, K, cnt+1)


A, K = map(int,input().split())
result = 1e9
dp = [1e9] * 1000001
make_number(A,K,0)


print(result)