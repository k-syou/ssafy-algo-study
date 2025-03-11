def find(arr, i, connected, wire_length):
    global max_connected, min_wire_length
     
    if i >= len(cores):  # 모든 코어를 검사했을 때
        if connected > max_connected or (connected == max_connected and wire_length < min_wire_length):
            max_connected = connected
            min_wire_length = wire_length
        return
     
    r, c = cores[i]
     
    # 네 방향으로 전선 설치 시도
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        temp_arr = [row[:] for row in arr]
        cnt = 0
         
        # 전선 설치 가능 여부 확인
        while 0 <= nr < N and 0 <= nc < N:
            if temp_arr[nr][nc] != 0:
                break
            temp_arr[nr][nc] = 2  # 전선 표시
            nr += dr
            nc += dc
            cnt += 1
        else:  # 정상적으로 끝까지 연결된 경우
            find(temp_arr, i + 1, connected + 1, wire_length + cnt)
         
    # 연결하지 않고 다음 코어로 진행 (백트래킹)
    find(arr, i + 1, connected, wire_length)
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    cores = []
    for r in range(1, N-1):
        for c in range(1, N-1):
            if arr[r][c] == 1:
                cores.append((r, c))
     
    max_connected = 0
    min_wire_length = float('inf')
     
    find(arr, 0, 0, 0)
    print(f'#{tc} {min_wire_length}')