N, M = input().split()
M = int(M)
L = len(N)
# 내림차순 정렬
nums = sorted(map(int, input().split()), reverse=True)

# 각 숫자별 최대 값
# 1 5 7
# mapping = {'0': '0', '1': '1', '2': '1', '3': '1', '4': '1', '5': '5', '6': '5', '7': '7', '8': '7', '9': '7'}
mapping = {str(i):'' for i in range(10)}
x = 9
for num in nums:
    for i in range(x, num - 1, -1):
        mapping[str(i)] = str(num)
    x = num - 1
'''
8763 3
100000000


7 8 9

기본값 
099999999
'''
# 기본값 999

def make_max_num(i):
    num = N[i]  # i == 0 num = 8
    mv = mapping[num]  # mv = 8
    if mv == '0' and i > 0:
        return ""
    if i + 1 == L:  # 마지막 인덱스
        return mv
    
    if num > mv:  # 나보다 최대값이 작을 때
        return mv + mapping['9'] * (L - i - 1)
    else:  # 나랑 같을 때
        res1 = make_max_num(i + 1)
        if len(res1) == (L - i - 1):
            return mv + res1
        mv = mapping[str(int(num) - 1)]
        return mv + mapping['9'] * (L - i - 1)

print(int(make_max_num(0)))

def make_max_num(i):
    num = N[i]  # i == 1 num = 7
    mv = mapping[num]  # mv = 7
    if mv == '0' and i > 0:
        return ""
    if i + 1 == L: 
        return mv
    
    if num > mv:  # 나보다 최대값이 작을 때
        return mv + mapping['9'] * (L - i - 1)
    else:  # 나랑 같을 때
        res1 = make_max_num(i + 1) # 
        if len(res1) == (L - i - 1):
            return mv + res1
        mv = mapping[str(int(num) - 1)]
        return "" + mapping['9'] * (L - i - 1)
