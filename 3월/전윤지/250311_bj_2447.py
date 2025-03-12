"""별찍기"""


def recur(n):
    if n == 1:
        return ["*"]
    star = recur(n // 3)
    print(f"n은 {n}")

    stars = []
    for i in star:
        stars.append(i * 3)
        print(f"i는 {i}입니다")
        print(f"stars는 {stars}")
    for j in star:
        stars.append(j + " " * (n // 3) + j)
        print(f"j는 {j}입니다")
        print(f"stars는 {stars}")
    for k in star:
        stars.append(k * 3)
        print(f"k는 {k}입니다")
        print(f"stars는 {stars}")

    return stars


N = int(input())
print("\n".join(recur(N)))
