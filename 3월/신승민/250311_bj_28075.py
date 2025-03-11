def dmfkckck(day, now_place, now_score):
    global cnt
    if day == N:
        if now_score >= M:
            cnt += 1
            return
        else:
            return
    ns = now_score

    for miss in range(2):
        for place in range(3):
            p = score[miss][place]
            if place == now_place:
                p = score[miss][place] / 2
            ns += p
            dmfkckck(day+1, place, ns)
            ns -= p

N, M = map(int, input().split())
score = list(list(map(int, input().split())) for _ in range(2))
cnt = 0

dmfkckck(0, -1, 0)

print(cnt)