def dp(n, k):
    global result
    
    while k >= 2*n:
        if k % 2:
            k -= 1
            result += 1
        k //= 2
        result += 1
    if k == n:
        return
    result += k - n
    return

A, K = map(int, input().split())
result = 0
dp(A, K)
print(result)