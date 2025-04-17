def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return 0
    
    parents[root_x] = root_y
    return 1

people_num, party_num = map(int, input().split())
know_num, *knows = map(int, input().split())

parents = [0] + [i for i in range(1, people_num+1)]
for i in range(1, know_num):
    union(knows[i-1], knows[i])
print(parents)

result = 0
if know_num == 0:
    for _ in range(party_num): a = input()
    result = party_num
    print(result)

if know_num > 0:
    check_list = []
    for _ in range(party_num):
        party_member_num, *party_member = map(int, input().split())
        for i in range(1, party_member_num):
            union(party_member[i], party_member[i-1])
        check_list.append(party_member[0])
    
    # result = 0
    for check in check_list:
        if find(check) == find(knows[0]): # 부모가 같다면
            continue
        result += 1
    print(result)