def star(n):
    if n == 1:
        return ['*']
    b_num = n // 3
    before = star(b_num)
    after = []
    for i in range(n):
        idx = i % b_num
        if i // b_num == 1:
            add_str = before[idx] + ' ' * b_num + before[idx]
        else:
            add_str = before[idx] * 3
        after.append(add_str)
    return after

print(*star(int(input())), sep='\n')
