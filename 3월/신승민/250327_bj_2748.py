def fibo(i):
    for j in range(2, i + 1):
        arr[j] = arr[j-1] + arr[j-2]
    
N = int(input())
arr = [0] * (N + 1)
arr[1] = 1
fibo(N)

print(arr[N])