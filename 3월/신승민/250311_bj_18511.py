def dmdkr(l):
    global max_value
    
    if l == len(N):
        if max_value < ''.join(value) <= N:
            max_value = ''.join(value)
            return
        else:
            return
    
    
    for i in range(len(num)):
        value[l] = num[i]
        dmdkr(l+1)
        value[l] = 0
    

N, K = input().split()
num = list(input().split())
K = int(K)
max_value = '0' * len(N)

value = ['0'] * len(N)
if N[0] < min(num) or N[:2] < min(num)*2:
    dmdkr(1)
else:
    dmdkr(0)
print(int(max_value))
