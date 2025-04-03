# 시간 초과
def dfs(cnt, s, now):
    global is_result, result 

    if cnt == N: # 만약 모든 구슬을 정렬했다면
        if is_result[int(s[N//2])] == True: # 만약 중간에 있는 구슬이 True로 이미 제외되었다면
            pass
        else:
            is_result[int(s[N//2])] = True # True로 바꿔주고(답이 될 수 없음)
            result -= 1 # 총 후보군에서 제외
        return
    
    for i in range(1, N+1): # 구슬들을 하나씩 살펴보면서
        if i == now: # 현재와 같은 구슬이라면 pass
            continue
        if visited[i]: # 이미 앞에 정렬했다면 pass
            continue
        if i in not_next[now]: # 이 부분이 굳이 필요 없을 듯
            continue
        
        t = False # 해당 숫자가 앞에 있는 숫자들 뒤에 올 수 있다
        for c in range(len(s)-1): # 이전 정렬한 숫자들을 보면서 비교하자
            char = s[c] 
            if i in not_next[int(char)]: # 앞에 있는 숫자의 뒤에 못 오는 리스트에 있는 값이라면
                t = True # 해당 숫자가 앞에 있는 숫자들 뒤에 올 수 없다 -> continue
                break
        if t == True: continue  

        visited[i] = 1 
        dfs(cnt+1, s+str(i), i) # 다 통과하고 놓을 수 있다면 배열하고 다음으로 이동
        visited[i] = 0

N, M = map(int, input().split()) # 구슬 개수 N, 비교 횟수 M

light = [0] * (N+1)
heavy = [0] * (N+1) 

not_next = [[] for _ in range(N+1)] # 일렬로 가벼운 순부터 정렬할 때, 
                                    # idx의 오른쪽에 올 수 없는 값들

for _ in range(M):
    hv, lg = map(int, input().split()) # 무거운 것, 가벼운 것
    
    not_next[hv].append(lg) # hv의 오른쪽에 lg가 올 수 없다

is_result = [False] * (N+1) # 만약 중간에 올 수 있다면 True로 바꾸기

visited = [0] * (N+1)
result = N # 중간에 올 수 없는 총 개수

dfs(0, '', 0) # cnt, s(문자열), now

print(result)