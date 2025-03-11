def star(N):
    if N == 1:
        return ['*']
    # 이전 별 모양
    before_star = star(N // 3)
    result = []
    # 맨 위에 세번 반복되는 패턴
    for i in range(N//3):
        print(N, before_star[i] * 3)
        result.append(before_star[i] * 3)
    # 가운데 한번 - 빈칸 - 한번
    for i in range(N//3):
        print(N, before_star[i] + ' '*(N//3) + before_star[i])
        result.append(before_star[i] + ' '*(N//3) + before_star[i])
        pass
    # 마지막에 세번 반복되는 패턴
    for i in range(N//3):
        result.append(before_star[i] * 3)
        pass

    return result

# N = int(input())
N = 27
# for s in star(N):
#     print(s)

print(*star(N), sep='\n')
# print(star[0], star[1], ... star[n-1])