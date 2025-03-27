import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

copy_num = num.copy()

    
p = 0
for i in range(1, N):
    copy_num[i] += copy_num[i-1]
    
    copy_num[i-1] -= p
    if p > num[i]:
        p= num[i]
copy_num[N-1] -= p
# p, s = 0, 0
# for i in range(N):
    
#     if copy_num[i] >= 0:
#         copy_num[i] -= s
#     if num[i] < p:
#         s += p
#         p = num[i]
        

print(copy_num)
print(max(copy_num))
