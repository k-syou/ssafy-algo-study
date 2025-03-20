import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def A_to_K(num, cnt):
    nums = {A}
    q = deque([(A, 0)])

    while q:
        num, cnt = q.popleft()

        if num == K:
            return cnt
        
        if num +1 <= K and num + 1 not in nums:
            nums.add(num+1)
            q.append((num+1, cnt+1))

        if num *2 <= K and num * 2 not in nums:
            nums.add(num*2)
            q.append((num*2, cnt+1))

A, K = map(int, input().split())
print(A_to_K(A, K))
