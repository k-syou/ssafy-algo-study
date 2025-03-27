'''피보나치수2'''

'''def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
'''
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())
print(fibo2(n))