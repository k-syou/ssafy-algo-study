import sys
sys.stdin = open('input.txt')

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(a)
    return parent[a]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root

def game():
    global result
    temp = 0
    for _ in range(M):
        a, b = list(map(int, input().split()))
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            result = temp
            return
        union(a, b)
        temp+=1

result = 0

N, M = list(map(int, input().split()))
parent = [i for i in range(N)]
game()
print(result)