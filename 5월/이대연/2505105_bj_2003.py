## 이건 왜 시간초과일까? - for문을 돌아서?!
N, M = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(N+1):
    for j in range(i+1,N+1):
        sum_v = sum(arr[i:j])
        print(sum_v, cnt)
        if sum_v == M:
            cnt += 1
            break
print(cnt)

N, M = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 1
cnt = 0

while right <= N and left<=right:
    total = sum(arr[left:right])
    print(left, right, total)
    if total == M:
        cnt+=1
        right += 1

    elif total < M:
        right += 1
    else:
        left += 1
print(cnt)