"""
<문제요약>
규칙을 유추하여 별을 찍어보세요
n = 1
*

n = 2
*****
*
* ***
* * *
* * *
*   *
*****

n = 3
*********
*
* *******
* *     *
* * *** *
* * * * *
* * * * *
* *   * *
* ***** *
*       *
*********
<입력>
N = 번호

<알고리즘>
재귀
"""

N = int(input())


def write_stars(n):
    if n == 1:
        return ["*"]
    if n == 2:
        return [
            "*****",
            "*    ",
            "* ***",
            "* * *",
            "* * *",
            "*   *",
            "*****",
        ]
    # 이전 번호 별 문자열 배열 가져오기
    prev_stars = write_stars(n - 1)

    # 첫줄 마지막줄 개수
    # 1 : 1, 2 : 5, 3 : 9, 4 : 13 ...
    # 4씩 증가함
    line_length = (n - 1) * 4 + 1
    result = []
    # 첫 출
    result.append("*" * line_length)
    # 두번째 줄
    result.append("*" + " " * (line_length - 1))
    # 전 별 문자 배열에 겹치는 부분
    for i in range(len(prev_stars)):
        s = "* " + prev_stars[i]
        if i == 0:
            s += "**"
        else:
            s += " *"
        result.append(s)
    # 뒤에서 두번째 줄
    result.append("*" + " " * (line_length - 2) + "*")
    # 마지막줄
    result.append("*" * line_length)
    return result


# 공백 제거 후 출력
print(*map(lambda s: s.strip(), write_stars(N)), sep="\n")
