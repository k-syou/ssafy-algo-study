N, M = input().split()
M = int(M)
L = len(N)
# 내림차순 정렬
nums = sorted(map(int, input().split()), reverse=True)

# 각 숫자별 최대 값
# 1 5 7
# mapping = {'0': '0', '1': '1', '2': '1', '3': '1', '4': '1', '5': '5', '6': '5', '7': '7', '8': '7', '9': '7'}
mapping = {str(i):'0' for i in range(10)}
x = 9
for num in nums:
    for i in range(x, num - 1, -1):
        mapping[str(i)] = str(num)
    x = num - 1

def make_max_num(i):
    search_num = N[i]
    mapping_num = mapping[search_num]
    if mapping_num == '0' and i > 0:
        return ""
    if i + 1 == L:
        return mapping_num
    if search_num > mapping_num:
        return mapping_num + mapping['9'] * (L - i - 1)
    else:
        res1 = make_max_num(i + 1)
        if len(res1) == (L - i - 1):
            return mapping_num + res1
        mapping_num = mapping[str(int(search_num) - 1)]
        return mapping_num + mapping['9'] * (L - i - 1)

print(int(make_max_num(0)))