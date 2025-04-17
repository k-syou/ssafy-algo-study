def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
        return parents[a]
    else:
        return parents[a]
    
def union(nums):
    min_parent = min(find(num) for num in nums)
    for num in nums:
        parents[find(num)] = min_parent

# def union(a, b):
#     a_root = find(a)
#     b_root = find(b) 
#     if a_root < b_root:
#         parents[b_root] = a_root
#     else:
#         parents[a_root] = b_root


N, M = list(map(int, input().split()))
parents = [i for i in range(N+1)]
know_num, *know_idx = list(map(int, input().split()))
result_list = [0]*(N+1)

for i in know_idx:
    parents[i]=0

for i in range(M):
    K, *nums = list(map(int, input().split()))
    union(nums)
    result_list[find(nums[0])]+=1
# print(parent)
# print(result_list)
result = 0
for i in range(N+1):
    if find(i) != 0:
        result += result_list[i]
print(result)