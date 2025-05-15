# 문제
# 테트리스는 아래와 같은 5가지 조각으로 이루어져 있다. 
# 정수로 이루어진 N×N 표가 주어진다. 테트리스 블록 중 하나를 표에 놓아 블록 아래에 있는 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.
# 모든 테트리스 블록은 90도씩 회전시킬 수 있다. 일부 조각은 총 4가지 형태를 가질 수 있다. 블록이 모두 표 안에 들어있는 형태는 모두 가능한 형태이다.

# 예를 들어, 가장 왼쪽 블록을 첫 행에 놓으면 합 80을 얻을 수 있다. 90도 회전시켜 셋째 열에 놓으면 91을 얻을 수 있다.

# 표의 크기가 4×4인 경우에 블록을 놓는 방법의 수는 총 77가지이다. 위의 예제에서 가장 큰 합은 120이다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 표의 크기 N이 주어지고, 4 ≤ N ≤ 100을 만족한다. 둘째 줄부터 표에 쓰여 있는 숫자가 주어진다. 숫자는 절댓값이 1,000,000을 넘지 않는 정수이다.

# 입력의 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스 마다, 케이스 번호를 출력하고 가장 큰 합을 출력한다.

'''
입력
4 
70  2  1 7
 7  1 30 6 
 4 30 30 5 
 3  1 30 2 
0

출력
1. 120
'''

import sys
input = sys.stdin.readline
test_case = 0

def get_prefix(matrix, n):
    prefix = [row[:] for row in matrix]
    for i in range(n):
        for j in range(n):
            if i:
                prefix[i][j] += prefix[i - 1][j]
            if j:
                prefix[i][j] += prefix[i][j - 1]
            if i and j:
                prefix[i][j] -= prefix[i - 1][j - 1]
    return prefix


def cal_prefix(prefix, sy, sx, len_y, len_x):
    result = prefix[sy][sx]
    dy = sy - len_y
    dx = sx - len_x
    if dy >= 0:
        result -= prefix[dy][sx]
    if dx >= 0:
        result -= prefix[sy][dx]
    if dy >= 0 and dx >= 0:
        result += prefix[dy][dx]
        
    return result


block_2_3 = [
    [(0, 0), (0, 2)],
    [(0, 1), (0, 2)],
    [(1, 0), (1, 2)],
    [(0, 2), (1, 0)],
    [(1, 0), (1, 1)],
]
block_3_2 = [
    [(1, 1), (2, 1)],
    [(0, 0), (1, 0)],
    [(0, 0), (2, 0)],
    [(0, 1), (2, 1)],
    [(0, 0), (2, 1)]
]

while True:
    N = int(input())
    if N == 0:
        break
    test_case += 1
    
    matrix = [[*map(int, input().split())] for _ in range(N)]
    prefix = get_prefix(matrix, N)
    max_value = float('-inf')
    for i in range(N):
        for j in range(N):
            # (i, j) 위치가 가장 왼쪽 위 라고 했을 때 나올 수 있는 모든 모양 확인
            
            # 2 x 3 블럭에서 나올 수 있는 모든 블럭 모양 별 합 확인
            if i + 1 < N and j + 2 < N:
                sum_2_3 = cal_prefix(prefix, i + 1, j + 2, 2, 3)
                for loc_a, loc_b in block_2_3:
                    sum_curr = sum_3_2 - matrix[i+loc_a[0]][j+loc_a[1]] - matrix[i+loc_b[0]][j+loc_b[1]]
                    max_value = max(max_value, sum_curr)
            
            # 3 x 2 블럭에서 나올 수 있는 모든 블럭 모양 별 합 확인
            if i + 2 < N and j + 1 < N:
                sum_3_2 = cal_prefix(prefix, i + 2, j + 1, 3, 2)
                for loc_a, loc_b in block_3_2:
                    sum_curr = sum_3_2 - matrix[i+loc_a[0]][j+loc_a[1]] - matrix[i+loc_b[0]][j+loc_b[1]]
                    max_value = max(max_value, sum_curr)
            
            # 2 x 2 블럭 합 확인
            if i + 1 < N and j + 1 < N:
                sum_2_2 = cal_prefix(prefix, i + 1, j + 1, 2, 2)
                max_value = max(max_value, sum_2_2)
                
            # 1 x 4 블럭 합 확인
            if j + 3 < N:
                sum_1_4 = cal_prefix(prefix, i, j + 3, 1, 4)
                max_value = max(max_value, sum_1_4)
            
            # 4 x 1 블럭 합 확인
            if i + 3 < N:
                sum_4_1 = cal_prefix(prefix, i + 3, j, 4, 1)
                max_value = max(max_value, sum_4_1)

    print(f'{test_case}. {max_value}')
