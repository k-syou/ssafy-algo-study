"""
스파이
"""

"""
---------------------------1t------------------------------------
def dfs(day, sum, prev):
    global cnt

    if day == N:  # 모든 임무 완료 했을 때
        if sum >= M:
            cnt += 1
            return
            ????리턴은 어디서 해???
            

    for work in range(2):
        for place in range(3):
            advance = sum

            if place == prev:
                advance += mission[work][place] / 2
            else:
                advance += mission[work][place]
                dfs(day + 1, advance, place)
                ?????여기서 호출해도 돼?
-------------------------------------------------------------------
"""

N, M = map(int, input().split())  # N: 임무 요일, M: 최소 진척도
mission = [list(map(int, input().split())) for _ in range(2)]  # 수행임무 - 진척도
cnt = 0


def dfs(day, sum, prev):
    global cnt

    # 경우의 수 돌아 봤을 때 M보다 크면 cnt +1
    if day == N:  # 모든 임무 완료 했을 때
        if sum >= M:
            cnt += 1
        return

    for work in range(2):
        for place in range(3):
            advance = sum

            if place == prev:
                advance += mission[work][place] / 2
            else:
                advance += mission[work][place]

            dfs(day + 1, advance, place)


dfs(0, 0, -1)
print(cnt)
