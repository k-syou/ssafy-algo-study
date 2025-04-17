import sys
from collections import deque

input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        if x_root in truth_people_info:
            parents[y_root] = x_root
        else:
            parents[x_root] = y_root


N, M = map(int, input().split())
truth_people_info = list(map(int, input().split()))
truth_people_info.pop(0)

parents = list(range(N+1))
parties = []
for _ in range(M):
    party_info = deque(list(map(int, input().split())))
    for i in range(1, party_info[0]):
        a, b = party_info[i], party_info[i+1]
        union(a, b)
    party_info.popleft()
    parties.append(party_info)

can_go = set()
for p in parents:
    if p not in truth_people_info:
        if p != 0:
            can_go.add(p)
            
res = 0
for party in party_info:
    if party in can_go:
        res += 1
        
print(parents)
print(can_go)
print(res)
print(parties)