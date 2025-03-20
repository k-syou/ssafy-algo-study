A, K = map(int, input().split())
cnt = 0

while K > A:  # K가 A보다 크면 연산 계속할거야
    if K % 2 == 0 and K // 2 >= A:  # K가 짝수이고, 나눠도 A보다 크면 진행해 나눠도 돼
        K //= 2
    else:  # 그렇지 않으면
        K -= 1  # 2의 배수 될때까지 빼

    cnt += 1  # 나누기나 빼기 둘 중 하나 할때마다 cnt up

print(cnt)
