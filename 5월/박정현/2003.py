# import sys
# sys.stdin=open("input.txt", 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
cnt = 0

while right <= N and left<=right:
    total = sum(arr[left:right])
    # print(arr[left:right])

    if total == M:
        cnt+=1
        right += 1
        # print(cnt)
    elif total < M:
        right += 1
    else:
        left += 1

print(cnt)
