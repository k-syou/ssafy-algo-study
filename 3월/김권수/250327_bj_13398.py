N = int(input())
INF = float("inf")
arr = [*map(int, input().split())]
# dp[i][0] : i번 수까지 숫자 삭제를 사용하지 않은 경우 가장 큰 값
# dp[i][1] : i번 수까지 숫자 삭제를 한번 사용한 경우 가장 큰 값
dp = [[-INF, -INF] for _ in range(N)]
dp[0][0] = arr[0]
dp[0][1] = 0

for i in range(1, N):
    # 이전 누적에 이어서 합산 vs 현재 번호부터 누적
    dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
    # 이전 번호에서 사용하고 현재 값 누적 vs 현재 번호부터 값삭제를 사용 vs 현재 번호부터 값 삭제를 사용하고 누적
    dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0], 0)

# dp 배열중 가장 큰값 할당
result = max(map(max, dp))

# result 가 0인경우 arr의 값이 모두 음수일 가능성이 있다.
# 그런 경우 아무것도 선택하지 않은 것을 결과로 표출 할 수 있다.
# 그러므로 0인경우 arr에서 하나만 선택한 경우중 가장 큰수를
# 결과값으로 설정한다.
if result == 0:
    result = max(arr)
print(result)
